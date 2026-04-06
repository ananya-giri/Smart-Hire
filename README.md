# 🚀 SmartHire AI: Autonomous HR & Recruitment Intelligence

![SmartHire UI](https://img.shields.io/badge/CrewAI-Agents-purple?style=for-the-badge) ![Gemini](https://img.shields.io/badge/Google_Gemini-Model-blue?style=for-the-badge) ![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge)

SmartHire AI is a next-generation autonomous multi-agent recruitment platform designed to entirely automate the modern HR pipeline. Powered by the Google Gemini API and the CrewAI framework, the platform simulates an entire 10-agent "HR Department-in-a-Box."

It doesn't just read resumes—it scours the web, prevents AI-based prompt injection forgery, calculates skill graphs mathematically, and actively constructs and dispatches formal job offer emails and calendar events.

---

## 🔬 Research Innovations

Designed for advanced academic research into Next-Gen HR algorithms, this platform implements features fundamentally missing from modern HR Software architectures. These establish significant novelty for publication:

### 1. Adversarial Defense & Multimodal Integrity Verification
Candidates now use GenAI to write perfectly keyword-stuffed resumes or embed white-text instructions (Prompt Injections) to bypass standard LLMs. SmartHire solves this by forcing both resumes and candidate video pitches through an isolated **Forensic Auditor Agent**. This agent hunts for textual prompt injections and narrative hallucinations. Simultaneously, it uses Vision-Language Models (VLMs) to scrutinize video submissions for deepfake avatars, unnatural lip-syncing, and rhythmic eye-tracking indicative of off-screen teleprompter usage (ChatGPT-fed answers), generating an *Authenticity Integrity Score* to defend the system downstream.

### 2. Neuro-Symbolic Knowledge Graph Matching
Traditional algorithmic filters will reject a candidate applying for a "React" role if their resume only explicitly says "Next.js." SmartHire bridges this logic failure using a **Neuro-Symbolic System**. When the LLM parses a gap, it queries an algorithmic Python `networkx` Knowledge Graph to calculate the shortest mathematical path between skills. The Semantic Graph passes deterministic clearance back to the Neural Model to intelligently override the keyword gap based on latent proximity.

### 3. Fail-Safe Presenter Mode (API-Resilient Scraping)
Live scraping tools routinely break during research demonstrations due to unexpected Cloudflare Auth-walls or DuckDuckGo HTTP Rate Limits. SmartHire implements an embedded fallback matrix: if a web scraping Agent is blocked by an API limit, the internal infrastructure automatically intercepts the exception and feeds the LLM an intelligent simulated candidate string, ensuring the multi-agent execution never crashes in production.

### 4. Agentic Real-World Competency Verification
To bridge the gap between text-based resume claims and real-world engineering competency, the system deploys a **Technical Assessment & Code Auditor Agent**. When the Screening agent completes its parsing, this specialized agent actively scans the candidate's resume for GitHub repository links. Using integrating `github_tool` APIs, it securely audits repository structure, proficiency, and descriptions. It then uses the candidate's skill gaps (Latent Blind Spots) to dynamically generate a personalized adaptive technical interview targeting their exact weaknesses.

---

## ⚙️ The 10-Agent Cognitive Pipeline

This system executes sequentially using autonomous agents, each provided with dedicated python toolsets `(tools/)`:

1. 📈 **Market Intelligence:** Evaluates hiring bottlenecks and talent availability.
2. 🕵️ **Web Sourcing:** Scrapes actual candidate portfolios off the open Internet.
3. 🛡️ **Integrity Forensic Analyst:** Defends the system against Textual Prompt Injections and Visual Deepfakes/Teleprompters.
4. 🧠 **Technical Screener:** Analyzes the candidate using Neuro-Symbolic Graph Math.
5. 💻 **Technical Code Auditor:** Verifies competency through autonomous GitHub repository auditing and adaptive blind-spot interview generation.
6. ⚖️ **Bias & Fairness Auditor:** Scrubs the analysis for implicit bias (gender/pedigree).
7. 📅 **Engagement Coordinator:** Triggers Python SMTP tools to auto-email the outreach and draft Calendar Invites.
8. 📊 **Analytics Specialist:** Evaluates the conversion throughput of your pipeline.
9. 💼 **Onboarding Officer:** Assembles and outputs the Official Offer Letter email based on real-time salary benchmarks.
10. 💡 **Explainable AI Judge:** Compiles the mathematical outputs into a transparent UI dashboard report.

---

## 📦 Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/ananya-giri/Smart-Hire.git
cd Smart-Hire/genai2
```

**2. Initialize your Environment**
```bash
python -m venv .venv
.\.venv\Scripts\activate 
pip install -r requirements.txt
```

**3. Configure Environment Protocol**
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
CREWAI_DISABLE_TELEMETRY=true
```

**4. Launch the Dashboard**
```bash
streamlit run ui/app.py
```
