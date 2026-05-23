from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import shutil
from main import run_recruitment_flow, save_to_vault, search_vault, get_all_vault_resumes
from tools.pdf_processor import extract_text_from_pdf
from security_guardrails import AIHiringGuardrails

app = FastAPI(title="Smart Hire API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str
    context: str

@app.post("/analyze")
async def analyze_candidate(
    job_desc: UploadFile = File(...),
    email: str = Form(...),
    resume: UploadFile = File(...)
):
    try:
        temp_file = f"temp_{resume.filename}"
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)
            
        resume_text = extract_text_from_pdf(temp_file)
        
        # Calculate Job Description
        temp_jd_file = f"temp_{job_desc.filename}"
        with open(temp_jd_file, "wb") as buffer:
            shutil.copyfileobj(job_desc.file, buffer)
            
        if temp_jd_file.lower().endswith('.pdf'):
            job_desc_text = extract_text_from_pdf(temp_jd_file)
        else:
            with open(temp_jd_file, "r", encoding="utf-8") as f:
                job_desc_text = f.read()
        
        # --- INPUT GUARDRAILS ---
        # 1. Block adversarial prompt injections from candidates
        AIHiringGuardrails.detect_prompt_injections(resume_text)
        AIHiringGuardrails.detect_prompt_injections(job_desc_text)
        
        # 2. Meta's Llama Guard 3 check
        AIHiringGuardrails.llama_guard_check(resume_text)
        
        # 3. Privacy Guardrail: Redact PII before sending to external CrewAI agents
        safe_resume_text = AIHiringGuardrails.redact_pii(resume_text)
        # -------------------------
        
        # Run CrewAI flow
        crew_result = await run_recruitment_flow(
            safe_resume_text,
            job_desc_text,
            email if email else "candidate@example.com"
        )
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
        if os.path.exists(temp_jd_file):
            os.remove(temp_jd_file)
        
        return {"status": "success", "result": crew_result.raw}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/vault")
async def get_vault():
    return get_all_vault_resumes()

@app.post("/chat")
async def chat_with_hr_assistant(chat_msg: ChatMessage):
    try:
        # --- OUTPUT/TOPIC GUARDRAIL ---
        AIHiringGuardrails.enforce_hr_topic(chat_msg.message)
        AIHiringGuardrails.llama_guard_check(chat_msg.message)
        # ------------------------------
        
        from google import genai
        from config import GOOGLE_API_KEY
        
        client = genai.Client(api_key=GOOGLE_API_KEY)
        system_prompt = f"You are the internal HR Strategic Assistant. Context about the current actively screened candidate: {chat_msg.context}."
        full_prompt = f"{system_prompt}\n\nHR Recruiter Question: {chat_msg.message}"
        
        response = client.models.generate_content(
            model='gemini-flash-lite-latest',
            contents=full_prompt
        )
        return {"response": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
