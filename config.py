import os
import sys
from dotenv import load_dotenv

# Disable CrewAI telemetry immediately
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from crewai import LLM

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set standard keys
if GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GEMINI_API_KEY"] = GOOGLE_API_KEY

# We prioritize Groq for its high speeds and generous free tier limit as requested by the user.
# We default to Gemini because it has a massive free-tier rate limit of 1,000,000 Tokens Per Minute (TPM)
# which is essential for processing large resumes without hitting Groq's tight 12,000 TPM limit.
# However, if the user has a Groq paid plan and wishes to use it, they can set USE_GROQ=true in .env.
USE_GROQ = os.getenv("USE_GROQ", "false").lower() == "true"

if USE_GROQ and GROQ_API_KEY and not any(x in GROQ_API_KEY for x in ["your_groq_api_key_here", "PASTE_YOUR_KEY_HERE"]):
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.4,
        api_key=GROQ_API_KEY
    )
    print("[LLM CONFIG] Smart Hire configured to use Groq LLM (llama-3.3-70b-versatile).")
else:
    if not GOOGLE_API_KEY or any(x in GOOGLE_API_KEY for x in ["your_gemini_api_key_here", "PASTE_YOUR_KEY_HERE"]):
        print("\n[ERROR] GOOGLE_API_KEY not found or is still a placeholder.")
        print("Please open the '.env' file and configure a valid API key.")
        sys.exit(1)
    
    llm = LLM(
        model="gemini/gemini-flash-lite-latest",
        temperature=0.4,
        api_key=GOOGLE_API_KEY
    )
    print("[LLM CONFIG] Smart Hire configured to use Gemini LLM (gemini-flash-lite-latest).")

# Configuration for CrewAI Agents
AGENT_CONFIG = {
    "llm": llm,
    "verbose": True,
    "allow_delegation": False
}
