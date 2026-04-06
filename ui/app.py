import streamlit as st
import os
import sys
import time
import re

# Disable CrewAI telemetry immediately at startup to avoid thread/signal errors
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

# Add parent directory to path to import main logic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import run_recruitment_flow, save_to_vault, search_vault, get_all_vault_resumes, clear_vault
from tools.pdf_processor import extract_text_from_pdf

# --- Page Config ---
st.set_page_config(
    page_title="Smart Hire | Recruitment Intelligence",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Premium Styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #210635, #420D4B, #7B337E);
    color: #F5D5E0;
}

.main-header {
    background: linear-gradient(90deg, #F5D5E0, #6667AB, #7B337E);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: 3.5rem;
}

.subtitle {
    color: #F5D5E0;
    font-size: 1.1rem;
    opacity: 0.85;
}

.glass-card {
    background: rgba(66, 13, 75, 0.55);
    border-radius: 16px;
    padding: 1.8rem;
    backdrop-filter: blur(16px);
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">Smart Hire</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Recruitment Intelligence Platform</p>', unsafe_allow_html=True)

# --- Metrics Extraction ---
match_score = "--"
hiring_difficulty = "Pending"

if "last_result" in st.session_state and st.session_state.last_result:

    report_text = str(st.session_state.last_result.raw)
    
    # AI outputs are often split across multiple tasks, so we combine everything
    if hasattr(st.session_state.last_result, 'tasks_output'):
        for t in st.session_state.last_result.tasks_output:
            report_text += " " + str(t.raw)

    m1 = re.search(r"score.*?(\d{2,3})/100", report_text, re.IGNORECASE)
    m2 = re.search(r"(\d{2,3})/100", report_text)
    m3 = re.search(r"score.*?:\s*(\d{2,3})", report_text, re.IGNORECASE)
    m4 = re.search(r"fit score.*?(\d{2,3})", report_text, re.IGNORECASE)

    if m1: match_score = m1.group(1) + "%"
    elif m2: match_score = m2.group(1) + "%"
    elif m3: match_score = m3.group(1) + "%"
    elif m4: match_score = m4.group(1) + "%"

    # Match difficulty, looking for context around it first
    diff_match_exact = re.search(r"difficulty.*?:\s*(low|medium|high)", report_text, re.IGNORECASE)
    if diff_match_exact:
        hiring_difficulty = diff_match_exact.group(1).capitalize()
    else:
        difficulty_match = re.search(r"\b(Low|Medium|High)\b", report_text, re.IGNORECASE)
        if difficulty_match:
            hiring_difficulty = difficulty_match.group(1).capitalize()

# --- Metrics Row ---
metric1, metric2, metric3 = st.columns(3)

vault_data = get_all_vault_resumes()
candidate_count = 0

if vault_data and "documents" in vault_data:
    candidate_count = len(vault_data["documents"])

with metric1:
    st.metric("Candidates Processed", candidate_count)

with metric2:
    st.metric("Match Score", match_score)

with metric3:
    st.metric("Hiring Difficulty", hiring_difficulty)

st.markdown("---")

# --- Sidebar ---
with st.sidebar:

    st.image("https://img.icons8.com/fluency/200/artificial-intelligence.png", width=120)
    st.title("Control Center")

    app_mode = st.radio("Navigation", ["🚀 New Analysis", "🗄️ Resume Vault", "💬 HR Assistant"])

    st.markdown("---")

    model_choice = st.selectbox(
        "Intelligence Engine",
        [
            "Gemini Flash Lite (Active Pipeline)", 
            "Gemini 2.0 Flash (Restricted Quota)", 
            "Gemini 1.5 Pro (Authwall)"
        ]
    )

    anonymize_mode = st.toggle("Strict Anonymization", value=True)

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# =====================================================
# 🚀 NEW ANALYSIS
# =====================================================

if app_mode == "🚀 New Analysis":

    col1, col2 = st.columns([1.2, 3.8], gap="large")

    with col1:

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Opportunity")

        default_jd = ""
        jd_path = "data/job_description.md"

        if os.path.exists(jd_path):
            with open(jd_path, "r") as f:
                default_jd = f.read()

        job_desc = st.text_area(
            "Job Description / Role Requirements",
            value=default_jd,
            height=350
        )

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Candidate")
        
        candidate_email = st.text_input("Candidate Email Address (for contact)", placeholder="candidate@example.com")

        uploaded_resume = st.file_uploader("Upload Resume", type=["pdf"])
        uploaded_video = st.file_uploader("Upload Intro Video (Optional)", type=["mp4", "mov", "avi"])

        if st.button("Run Intelligence Engine", use_container_width=True):

            if not job_desc or not uploaded_resume:
                st.error("Please provide both a Job Description and a Resume.")

            else:

                try:

                    with open("temp_resume.pdf", "wb") as f:
                        f.write(uploaded_resume.getbuffer())

                    resume_text = extract_text_from_pdf("temp_resume.pdf")

                    crew_result = run_recruitment_flow(
                        resume_text,
                        job_desc,
                        candidate_email if candidate_email else "candidate@example.com"
                    )

                    st.session_state.last_result = crew_result
                    st.session_state.current_resume_text = resume_text
                    st.session_state.current_filename = uploaded_resume.name

                except Exception as e:
                    st.error(str(e))

        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.last_result:

        st.markdown("## 📊 Strategic Recruitment Dossier")

        # Expose all intermediate AI agent task outputs (Sourcing, Web Scraping, Market Prediction, etc.)
        if hasattr(st.session_state.last_result, 'tasks_output'):
            st.markdown("### 🛠️ Agent Operations Logs (Web Scraping & Market Data)")
            
            # Map common task indices to names for easier reading (based on your sequential pipeline)
            task_names = [
                "Market Prediction",
                "Web Sourcing & Scraping",
                "CV Integrity & AI-Forgery Check",
                "Technical Screening",
                "Bias Detection",
                "Engagement Email & Scheduling",
                "Analytics",
                "Onboarding & Offer",
                "Management",
                "Final Explainability Report"
            ]
            
            for idx, task_out in enumerate(st.session_state.last_result.tasks_output):
                task_title = task_names[idx] if idx < len(task_names) else f"Task {idx+1}"
                with st.expander(f"🤖 Agent Task: {task_title}"):
                    st.markdown(task_out.raw)

        st.markdown("### 🏆 Final Analyst Hiring Decision")
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(st.session_state.last_result.raw)
        st.markdown('</div>', unsafe_allow_html=True)

        icol1, icol2 = st.columns(2)

        with icol1:

            st.download_button(
                label="📥 Download Intelligence Dossier",
                data=str(st.session_state.last_result.raw),
                file_name=f"recruitment_intelligence_{int(time.time())}.md",
                mime="text/markdown"
            )

        with icol2:

            if st.button("💾 Save Candidate to Vault"):

                import re
                full_text = str(st.session_state.last_result.raw)
                
                # AI scores are often stored in intermediate tasks (like Screening), so we must scan everything.
                if hasattr(st.session_state.last_result, 'tasks_output'):
                    for t in st.session_state.last_result.tasks_output:
                        full_text += " " + str(t.raw)

                ai_score = 0
                # Robust fallback pattern matching for unpredictable GenAI formatting
                m1 = re.search(r"score.*?(\d{2,3})/100", full_text, re.IGNORECASE)
                m2 = re.search(r"(\d{2,3})/100", full_text)
                m3 = re.search(r"score.*?:\s*(\d{2,3})", full_text, re.IGNORECASE)
                m4 = re.search(r"fit score.*?(\d{2,3})", full_text, re.IGNORECASE)

                if m1: ai_score = int(m1.group(1))
                elif m2: ai_score = int(m2.group(1))
                elif m3: ai_score = int(m3.group(1))
                elif m4: ai_score = int(m4.group(1))
                
                ai_score = min(max(ai_score, 0), 100) # Sanity bounds

                meta = {
                    "role": job_desc[:50],
                    "source": st.session_state.get("current_filename", "uploaded_resume"),
                    "ai_score": ai_score,
                    "timestamp": time.time()
                }

                try:
                    save_to_vault(
                        st.session_state.current_resume_text,
                        meta
                    )
                    st.toast("✅ Candidate safely archived in Vault!")
                except Exception as e:
                    st.error(f"❌ Failed to archive candidate to Vault: {e}")

# =====================================================
# 🗄️ RESUME VAULT
# =====================================================

elif app_mode == "🗄️ Resume Vault":

    st.markdown("## 🗄️ Talent Archive")

    search_query = st.text_input(
        "🔍 Search Vault",
        placeholder="e.g. React developer with ML experience"
    )

    if search_query:

        results = search_vault(search_query)

        st.subheader(f"Results for: {search_query}")

        if results and results["documents"]:

            for i, doc in enumerate(results["documents"][0]):

                similarity = round(1 - results["distances"][0][i], 2)
                ai_score = results["metadatas"][0][i].get("ai_score", "NA")

                with st.expander(
                    f"📄 Candidate {i+1} | AI Score: {ai_score}% | Search Similarity: {similarity}"
                ):
                    st.caption(f"AI Score: {ai_score}%")
                    st.caption(f"Search Similarity: {similarity}")
                    st.markdown(doc)
                    st.caption(f"Metadata: {results['metadatas'][0][i]}")

        else:
            st.info("No matching candidates found in the vault.")

# =====================================================
# 💬 HR ASSISTANT
# =====================================================

elif app_mode == "💬 HR Assistant":

    st.markdown("## 💬 HR Strategic Assistant")

    if not st.session_state.last_result:
        st.info("Run a new analysis first.")

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a question about this candidate's fit, salary, or skills...")

    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            try:
                from google import genai
                from config import GOOGLE_API_KEY
                
                client = genai.Client(api_key=GOOGLE_API_KEY)
                
                context = str(st.session_state.last_result.raw) if st.session_state.last_result else "No candidate Data."
                
                system_prompt = f"You are the internal HR Strategic Assistant. Context about the current actively screened candidate: {context}."
                full_prompt = f"{system_prompt}\n\nHR Recruiter Question: {prompt}"
                
                response = client.models.generate_content(
                    model='gemini-flash-lite-latest',
                    contents=full_prompt
                )
                
                st.markdown(response.text)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                st.error(f"Failed to connect to HR AI: {e}")

# --- Footer ---
st.markdown("""
<div style="text-align:center;color:#F5D5E0;font-size:0.8rem;">
Powered by <b>CrewAI</b> + <b>Google Gemini</b><br>
Built for Ethical & Data-Driven Hiring
</div>
""", unsafe_allow_html=True)