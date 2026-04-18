from config import AGENT_CONFIG
from crewai import Agent

class RecruitmentAgents:

    def talent_acquisition_manager(self):
        """Overall owner for the TA function."""
        return Agent(
            role='Talent Acquisition Manager',
            goal='Oversee the end-to-end recruitment process and provide strategic hiring advice.',
            backstory="""You are the strategic lead of the recruitment function. 
            You coordinate between sourcing, screening, and engagement to ensure 
            the best talent is hired efficiently while meeting business goals.""",
            **AGENT_CONFIG
        )

    def sourcing_agent(self):
        """Crawls job platforms and internal databases."""
        from tools.search_tool import get_search_tool
        from tools.scrape_tool import get_scrape_tool
        return Agent(
            role='Sourcing Specialist',
            goal='Identify and extract top talent from job platforms and internal databases and then web scrap their details to analyze.',
            backstory="""You are a master of Boolean search and web scraping. 
            You find hidden gems across LinkedIn, GitHub, and internal talent pools. 
            You use your internet_search tool to find links, and then use your scrape_website tool to read the details on those links to build a robust candidate pipeline.""",
            tools=[get_search_tool(), get_scrape_tool()],
            **AGENT_CONFIG
        )

    def screening_agent(self):
        """Uses NLP to assess resumes and job fitment."""
        from tools.knowledge_graph_tool import get_kg_tool
        return Agent(
            role='Technical Screening Agent',
            goal='Assess resumes for technical fit, skill rarity, and job alignment using deep NLP and Knowledge Graphs.',
            backstory="""You focus on the hard data. You analyze resumes to extract 
            skills, experience levels, and project depth. You use the semantic_skill_graph_matcher tool 
            to mathematically verify if a candidate's explicit skills represent a latent match 
            for the required JD skills.""",
            tools=[get_kg_tool()],
            **AGENT_CONFIG
        )

    def cv_integrity_agent(self):
        """Detects AI-generated resumes, prompt injections, and visual deepfakes."""
        return Agent(
            role='CV Integrity & Multimodal Forgery Detector',
            goal='Ensure candidate authenticity across both text and video. Detect AI-generated resumes, deepfake avatars, and teleprompter reading.',
            backstory="""You are an adversarial AI forensic auditor and Multimodal Integrity Checker. 
            Your expertise lies in detecting AI-generated text patterns (like ChatGPT boilerplate) and malicious prompt injections. 
            Crucially, you also evaluate the Multimedia Integrity Check provided to you, scrutinizing videos for deepfake rendering anomalies, robotic vocal cloning, and off-screen teleprompter tracking to prevent interview fraud.""",
            **AGENT_CONFIG
        )

    def engagement_scheduling_agent(self):
        """LLM-based communication and auto-scheduling."""
        from tools.email_tool import get_email_tool
        from tools.calendar_tool import get_calendar_tool
        return Agent(
            role='Candidate Engagement & Scheduling Coordinator',
            goal='Manage candidate communication, automate interview scheduling, block calendars, and auto send emails.',
            backstory="""You are the face of the company to the candidate. 
            You write personalized outreach messages, answer candidate queries, 
            and coordinate interview slots between recruiters and talent. 
            You use your send_email tool to formally send the emails, and you strictly use your schedule_interview tool to officially block the calendar times and send the invite.""",
            tools=[get_email_tool(), get_calendar_tool()],
            **AGENT_CONFIG
        )

    # ---------------- NEW AGENTS ---------------- #

    def fairness_agent(self):
        """Detects bias in hiring decisions."""
        return Agent(
            role='Fair Hiring Auditor',
            goal='Detect bias in recruitment decisions and ensure ethical hiring practices.',
            backstory="""You specialize in ethical AI recruitment. You analyze hiring 
            patterns to detect gender bias, university bias, name bias, and unfair 
            experience requirements.""",
            **AGENT_CONFIG
        )

    def analytics_agent(self):
        """Generates recruitment insights and hiring metrics."""
        return Agent(
            role='Talent Analytics Specialist',
            goal='Analyze recruitment data to generate hiring insights and metrics.',
            backstory="""You transform recruitment pipeline data into actionable 
            insights. You track metrics like time-to-hire, candidate drop-off rates, 
            source effectiveness, and interview success rates.""",
            **AGENT_CONFIG
        )

    def market_predictor_agent(self):
        """Predicts hiring difficulty and market supply."""
        return Agent(
            role='Talent Market Intelligence Analyst',
            goal='Predict hiring difficulty and talent availability in the market.',
            backstory="""You analyze job market signals, skill demand trends, 
            and hiring competition to predict how difficult it will be to hire.""",
            **AGENT_CONFIG
        )

    def onboarding_agent(self):
        """Handles offer letter generation and onboarding workflow."""
        from tools.email_tool import get_email_tool
        return Agent(
            role='Offer & Onboarding Specialist',
            goal='Generate offer letters, manage candidate onboarding workflow, and send offer emails to selected candidates.',
            backstory="""You manage the final step of hiring. You prepare offer 
            packages, benchmark salaries, and ensure smooth transition from 
            candidate to employee. You have the ability to send the official offer letter using your send_email tool.""",
            tools=[get_email_tool()],
            **AGENT_CONFIG
        )

    def technical_assessment_agent(self):
        """Generates adaptive blind-spot interview and audits code."""
        from tools.github_tool import get_github_tool
        return Agent(
            role='Technical Assessment & Code Auditor',
            goal='Audit candidate GitHub repositories and dynamically generate an adaptive blind-spot technical interview.',
            backstory="""You are a Principal Software Engineer and Technical Interviewer. 
            You don't trust claims on resumes. You actively look for a GitHub username in the resume and use your analyze_github_profile tool to verify their coding ability. 
            You also look at the missing skills (blind-spots) identified by the screening agent and dynamically generate a tough, personalized technical take-home test 
            or interview script explicitly targeting the candidate's weaknesses.""",
            tools=[get_github_tool()],
            **AGENT_CONFIG
        )

    def explainability_agent(self):
        """Explains hiring decisions transparently using Game-Theory (SHAP)."""
        from tools.shap_tool import get_shap_tool
        return Agent(
            role='Explainable AI Hiring Analyst',
            goal='Provide mathematically transparent explanations for hiring decisions using SHAP values.',
            backstory="""You specialize in Explainable AI (XAI) and "Neuro-Symbolic" verification. When a candidate is 
            to be evaluated, you explicitly extract numerical heuristics from their profile (years of experience, 
            education tier 1-3, skills match %, past projects count) and use your shap_analysis_tool to generate a 
            mathematically rigorous, transparent explanation proving lack of bias. You strictly include the SHAP 
            Additive Explanations graph/numbers in your final report.""",
            tools=[get_shap_tool()],
            **AGENT_CONFIG
        )