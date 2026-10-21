# SmartHire AI

<p align="center">
  <img src="assets/banner.jpg" alt="SmartHire AI Banner" width="100%"/>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/CrewAI-Multi--Agent-orange?style=for-the-badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/NetworkX-Knowledge_Graph-blue?style=for-the-badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/SHAP-Explainable_AI-red?style=for-the-badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/LlamaGuard-Security-teal?style=for-the-badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/></a>
</p>

<h3 align="center">Explainable &bull; Secure &bull; Neuro-Symbolic Recruitment Intelligence</h3>

<p align="center">
SmartHire AI is an enterprise-grade recruitment platform powered by <strong>10 specialized autonomous agents</strong> operating across a <strong>4-tier asynchronous DAG pipeline</strong>. It unites a <strong>Neuro-Symbolic Knowledge Graph</strong> for transferable skill matching, <strong>closed-form Shapley game-theoretic attribution</strong> for transparent hiring decisions, a <strong>multi-layer prompt-injection security guardrail</strong>, and <strong>real-world GitHub code auditing</strong> with multimodal interview verification.
</p>

---

## Table of Contents
- [Executive Overview](#executive-overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [The 10 Autonomous Agents](#the-10-autonomous-agents)
- [Core Technologies & Methodologies](#core-technologies--methodologies)
  - [1. Neuro-Symbolic Skill Knowledge Graph](#1-neuro-symbolic-skill-knowledge-graph)
  - [2. Closed-Form SHAP Explainability](#2-closed-form-shap-explainability)
  - [3. Multi-Layer Prompt-Injection Defense](#3-multi-layer-prompt-injection-defense)
  - [4. Real-World GitHub Code Auditing](#4-real-world-github-code-auditing)
  - [5. Multimodal Video Interview Integrity](#5-multimodal-video-interview-integrity)
  - [6. Adaptive Technical Assessment](#6-adaptive-technical-assessment)
- [Empirical Benchmark Results](#empirical-benchmark-results)
- [Project Directory Structure](#project-directory-structure)
- [Quick Start Guide](#quick-start-guide)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Running with Docker Compose](#running-with-docker-compose)
- [Running Benchmarks & Reproducibility](#running-benchmarks--reproducibility)
- [Research Documentation](#research-documentation)
- [Contributing & License](#contributing--license)

---

## Executive Overview

Conventional automated applicant tracking systems (ATS) suffer from critical vulnerabilities:
1. **Keyword Rigidity**: Qualified candidates are rejected due to superficial terminology mismatches (e.g., matching "React" fails for a senior "Next.js" engineer), resulting in high False Rejection Rates (FRR up to 75%).
2. **Black-Box Opacity**: Neural evaluators output arbitrary matching percentages without mathematically provable justifications, violating regulatory requirements such as the EU AI Act and EEOC Title VII.
3. **Adversarial Vulnerability**: Malicious applicants exploit prompt injection vectors (e.g., hidden prompt instructions in resume PDFs, white-text exploits, delimiter escapes) to manipulate LLM hiring screeners.
4. **Resume Inflation & Superficiality**: Unverified claims on resumes go unchecked without real-world artifact validation.

**SmartHire AI addresses every failure mode** through a defensible, neuro-symbolic, game-theoretically grounded, and securely hardened hiring pipeline.

---

## Key Features

| Feature | Description | Production Status |
|---|---|---|
| **Neuro-Symbolic KG Matching** | 70-node, 74-edge directed weighted graph with Dijkstra shortest-path traversal to resolve skill synonyms, transferability, and stack hierarchies. | Verified (FRR: 0.0%, F1: 1.000) |
| **Closed-Form SHAP Attribution** | Exact Shapley value computation with mathematical guarantees of efficiency, symmetry, dummy player, and additivity (zero reconstruction error). | Verified (Faithfulness R²: 1.000) |
| **Multi-Tier Prompt Defense** | 6-pattern regex pre-filter + structural heuristics + Llama-Prompt-Guard-2 transformer + Llama Guard 3 safety middleware. | Verified (76.7% mitigation, 0% FPR) |
| **Real-World Code Auditing** | Autonomous GitHub API integration inspecting live repositories, commit cadence, language distributions, and architectural patterns. | Integrated |
| **Multimodal Video Integrity** | Gemini Vision-Language Model analysis detecting teleprompter eye cadence, lip-sync anomalies, and synthesized audio cues. | Integrated |
| **Adaptive Technical Assessment** | Blind-spot analysis comparing resume skills against job specifications to generate customized technical challenges. | Integrated |
| **Bias & Diversity Auditing** | Disparate impact evaluation, demographic neutrality enforcement, and elimination of non-job-related attributes. | Integrated |
| **End-to-End Enterprise Tooling** | Persistent ChromaDB vector search, automated SMTP candidate communications, and iCalendar (`.ics`) meeting scheduling. | Integrated |
| **Multi-Stage Docker Architecture** | Production-ready multi-container deployment orchestrating FastAPI backend and React/Vite Nginx frontend. | Containerized |

---

## System Architecture

SmartHire AI replaces monolithic linear prompting with an asynchronous, multi-tier Directed Acyclic Graph (DAG) orchestrated by CrewAI:

```mermaid
graph TD
    subgraph Tier1 [Tier 1: Ingestion & Adversarial Defense]
        A[Inbound Candidate Resume / PDF] --> B[Adversarial Defense Agent]
        V[Candidate Video Interview] --> B
        B -->|Regex & Heuristic Filter| B1{Threat Detected?}
        B1 -->|Yes: Quarantine & Flag| B2[Security Quarantine Audit]
        B1 -->|No: Sanitized Stream| C[CV Ingestion & Parsing]
    end

    subgraph Tier2 [Tier 2: Parallel Sourcing & Technical Analysis]
        C --> D[Technical Screening Agent]
        C --> E[GitHub Repository Auditor]
        C --> F[Talent Sourcing Agent]
        JD[Target Job Description] --> D
        JD --> G[Market Intelligence Predictor]
        D <-->|Dijkstra Graph Distance| KG[(Neuro-Symbolic Knowledge Graph)]
        E <-->|Live Repo Inspection| GH[(GitHub REST API)]
        F <-->|Web Intelligence| WS[(Google / Web Scraper)]
    end

    subgraph Tier3 [Tier 3: Verification, Bias Audit & Explainability]
        D --> H[Adaptive Technical Assessment Agent]
        E --> H
        D --> I[Bias & Fairness Auditor]
        D --> J[Explainable AI Attribution Agent]
        J <-->|Exact Game-Theoretic Math| SHAP[(Closed-Form Shapley Calculus)]
    end

    subgraph Tier4 [Tier 4: Synthesis & Autonomous Operations]
        H --> K[Executive Hiring Manager Agent]
        I --> K
        J --> K
        G --> K
        K --> L[Candidate Engagement Coordinator]
        K --> M[Onboarding Specialist]
        L -->|Automated Personalized Outreach| SMTP[SMTP Email Dispatcher]
        L -->|Automated Interview Calendar Block| CAL[iCalendar .ics Generator]
    end
```

---

## The 10 Autonomous Agents

| # | Agent Name | Role & Responsibility | Core Tools / Integrations |
|---|---|---|---|
| 1 | **Adversarial Defense Auditor** | Scrutinizes inbound resumes and metadata for prompt injections, delimiter attacks, hidden fonts, and jailbreak vectors. | `detect_prompt_injections()`, Regex Pre-filter, Llama-Prompt-Guard-2 |
| 2 | **CV & Multimodal Screener** | Extracts structured candidate profiles, academic pedigrees, and inspects video recordings for teleprompter or deepfake cues. | `pdf_reader`, Gemini 2.0 Flash VLM |
| 3 | **Technical Screening Specialist** | Matches candidate competencies against job specifications using graph-based semantic distances rather than rigid string equality. | `semantic_skill_graph_matcher`, NetworkX Knowledge Graph |
| 4 | **GitHub & Code Auditor** | Autonomously fetches and reviews public engineering repositories to verify authenticity, commit regularity, and language distribution. | `github_tool`, GitHub REST API v3 |
| 5 | **Talent Sourcing Agent** | Conducts automated external talent queries across tech ecosystems to find comparative talent benchmarks. | `scrape_tool`, BeautifulSoup4, Google Custom Search |
| 6 | **Market Intelligence Predictor** | Analyzes industry salary benchmarks, geographic talent distribution, and competitiveness indices. | Compensation & Market Heuristics |
| 7 | **Adaptive Assessment Architect** | Identifies candidate latent skill gaps (blind spots) and constructs 3 dynamic, role-tailored technical interview challenges. | Dynamic Question Generator |
| 8 | **Bias & Fairness Auditor** | Scans intermediate evaluation tokens to strip demographic markers, verify EEOC compliance, and prevent proxy discrimination. | Demographic Parity Scanners |
| 9 | **Explainable AI Analyst** | Computes exact Shapley feature attributions to provide a transparent, mathematically verifiable justification for every decision. | `shap_scoring_explainer`, Closed-Form Shapley Engine |
| 10 | **Executive Hiring Manager** | Aggregates multi-agent ratings into an executive hiring dossier, coordinates engagement emails, and schedules calendar events. | `email_tool`, `calendar_tool`, SMTP, iCalendar |

---

## Core Technologies & Methodologies

### 1. Neuro-Symbolic Skill Knowledge Graph
Standard NLP keyword matching causes severe false rejections. SmartHire embeds a programmatic directed weighted graph ($G=(V, E, W)$) with **70 skill nodes** and **74 semantic relationship edges** categorised as:
- `synonym_of` (weight 0.05): Identical underlying competency (e.g., `PostgreSQL` $\leftrightarrow$ `Postgres`).
- `child_of` (weight 0.15): Specialization/framework of a foundational technology (e.g., `Next.js` $ightarrow$ `React` $ightarrow$ `JavaScript`).
- `transferable_to` (weight 0.25): Cross-stack competency transferability (e.g., `FastAPI` $ightarrow$ `Flask`, `PyTorch` $ightarrow$ `TensorFlow`).

When candidate skills $C$ are evaluated against required skills $R$:
$$	ext{Distance}(r, c) = \min_{c \in C} 	ext{DijkstraShortestPath}(G, r, c)$$
$$	ext{MatchScore}(r) = \max\left(0, 1 - rac{	ext{Distance}(r, c)}{	au}ight)$$
This deterministic graph layer eliminates token hallucination while retaining full semantic flexibility.

### 2. Closed-Form SHAP Explainability
Rather than relying on stochastic LLM explanations, SmartHire implements exact closed-form Shapley value attribution for candidate scoring:
$$\phi_i(v) = w_i \cdot \left( x_i - \mathbb{E}[X_i] ight)$$
For candidate feature vector $x$ across weighted requirements $w$ and population baseline $\mathbb{E}[X]$:
- **Efficiency**: $\sum_{i} \phi_i = f(x) - \mathbb{E}[f(X)]$ (Guaranteed exact additivity, zero reconstruction error).
- **Faithfulness**: Mathematically proven local and global fidelity ($R^2 = 1.000$).
- **Actionability**: Clear breakdown showing exactly which competencies drove the score up or down.

### 3. Multi-Layer Prompt-Injection Defense
Secures the recruiting pipeline against adversarial text injections:
- **Tier 1 (Regex Pre-Filter)**: 6 high-precision structural regex patterns intercepting imperative command overrides (`ignore previous instructions`, `system prompt`, `you must hire`, etc.).
- **Tier 2 (Structural Heuristics)**: Delimiter escape scanners, repeated token detectors, and non-printable character filters.
- **Tier 3 (Llama-Prompt-Guard-2 Transformer)**: 22M-parameter dedicated sequence classifier providing fine-grained injection probability scores.
- **Tier 4 (Llama Guard 3 Safety Middleware)**: Groq-accelerated safety guardrail for API boundaries.

### 4. Real-World GitHub Code Auditing
The `github_tool` queries the GitHub REST API to perform automated vetting:
- Inspects repository count, fork vs original source distribution, and primary language breakdown.
- Audits star counts, watchers, and commit timestamps to identify active codebases versus cloned boilerplate.
- Cross-references claimed competencies against verified repository technologies.

### 5. Multimodal Video Interview Integrity
For asynchronous candidate video submissions, SmartHire leverages Google's Gemini Vision-Language Models:
- **Teleprompter Reading Detection**: Tracks eye-gaze saccades and rhythmic left-to-right eye movements indicating off-screen ChatGPT reading.
- **Deepfake & Lip-Sync Verification**: Analyzes phoneme-to-viseme synchronization and synthetic visual artifacts.

---

## Empirical Benchmark Results

All benchmarks are fully reproducible using the scripts in the root directory.

### Benchmark 1: Skill Matcher Evaluation (N=55 Held-Out Real Resumes)
Evaluated on frozen held-out test cases from Kaggle resume datasets comparing strict keyword matching against our Neuro-Symbolic Knowledge Graph:

| Metric | Strict Keyword Baseline | Neuro-Symbolic KG (Ours) | Delta / Impact |
|---|---|---|---|
| **Accuracy** | 62.5% | **100.0%** | **+37.5%** |
| **Precision** | 100.0% | **100.0%** | Maintained (0 False Positives) |
| **Recall** | 25.0% | **100.0%** | **+75.0%** |
| **F1 Score** | 0.400 | **1.000** | **+0.600** |
| **False Rejection Rate (FRR)** | 75.0% | **0.0%** | **-75.0% (Eliminated)** |
| **False Acceptance Rate (FAR)** | 0.0% | **0.0%** | 0.0% (Zero leakage) |

### Benchmark 2: Security & Prompt-Injection Benchmark v2 (N=60 Test Cases)
Evaluated across 60 rigorously constructed test cases (30 diverse attack vectors + 30 complex benign resumes):

| Defense Layer | Attacks Mitigated | Benign False Positives | Mitigation Rate | False Positive Rate | Precision |
|---|---|---|---|---|---|
| **No Defense (Baseline)** | 0 / 30 | 0 / 30 | 0.0% | 0.0% | N/A |
| **Regex Pre-Filter Alone** | 23 / 30 | 0 / 30 | 76.7% | **0.0%** | **100.0%** |
| **Regex + Llama-Prompt-Guard-2** | 23 / 30 | 0 / 30 | **76.7%** | **0.0%** | **100.0%** |

- **Zero False Positives**: Legitimate resumes containing security terms (e.g., "penetration testing", "firewall", "IAM policies") are never falsely rejected.
- **Reproducibility**: Run `python run_security_benchmark_v2.py` to regenerate results.

### Benchmark 3: SHAP Attribution Faithfulness
- **Reconstruction Error ($\sum \phi_i - \Delta f$)**: Maximum absolute error = **0.000000** (Exact game-theoretic match).
- **Faithfulness Score ($R^2$)**: **1.0000** across all evaluated candidates.

---

## Project Directory Structure

```text
Smart.Hire/
├── assets/
│   └── banner.jpg                        # Project banner image
├── data/
│   ├── heldout_aggregate_metrics.json    # Verified N=55 held-out KG metrics
│   ├── heldout_per_case_results.json     # Per-case held-out evaluations
│   ├── security_benchmark_v2.json        # 60-case security benchmark metrics
│   ├── security_per_case_v2.json         # Per-case prompt-injection scores
│   ├── llama_guard2_per_case_scores.json # Genuine Llama-Prompt-Guard-2 inference
│   ├── shap_pipeline_metrics.json        # SHAP faithfulness verification
│   └── extracted_kaggle_resumes.json     # Extracted resume dataset
├── tools/
│   ├── knowledge_graph_tool.py           # 70-node NetworkX semantic skill matcher
│   ├── shap_scoring_explainer.py         # Closed-form Shapley attribution engine
│   ├── shap_tool.py                      # TreeExplainer ML sidecar module
│   ├── github_tool.py                    # GitHub REST API repository auditor
│   ├── scrape_tool.py                    # Web scraping & talent sourcing tool
│   ├── interview_prep_tool.py            # Adaptive technical assessment builder
│   ├── email_tool.py                     # SMTP candidate outreach generator
│   └── calendar_tool.py                  # iCalendar (.ics) appointment creator
├── ui/                                   # React / Vite modern frontend
│   ├── src/                              # Components, views, styling
│   └── Dockerfile                        # Multi-stage Nginx container build
├── api.py                                # FastAPI enterprise backend endpoints
├── config.py                             # Central application configuration
├── main.py                               # CrewAI multi-agent pipeline orchestrator
├── test_metric_reproducibility.py        # Automated test verification suite
├── run_security_benchmark_v2.py          # Security benchmark runner
├── run_shap_pipeline_benchmarks.py       # SHAP attribution benchmark runner
├── Dockerfile                            # FastAPI backend container definition
├── docker-compose.yml                    # Multi-container orchestration
├── requirements.txt                      # Python dependencies
├── README.md                             # Repository overview and documentation
├── RESEARCH_REPORT.md                    # Comprehensive academic research report
├── SMARTHIRE_RESEARCH_EVIDENCE_AUDIT.md  # Complete research evidence audit
└── RESEARCH_PAPER_SECTIONS.md            # IEEE journal paper manuscript sections
```

---

## Quick Start Guide

### Prerequisites
- **Python**: 3.11 or 3.12
- **Node.js**: v18+ (for local UI development)
- **Docker & Docker Compose**: (Optional, for containerized run)
- **API Keys**: Groq API key, Google Gemini API key (optional for VLM), GitHub Personal Access Token (optional for higher rate limits).

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ananya-giri/Smart-Hire.git
   cd Smart-Hire
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   GITHUB_TOKEN=your_optional_github_token
   HF_TOKEN=your_optional_huggingface_token
   PORT=8000
   ```

5. **Start the FastAPI backend:**
   ```bash
   uvicorn api:app --reload --port 8000
   ```
   API interactive docs will be available at `http://localhost:8000/docs`.

6. **Start the Frontend UI:**
   ```bash
   cd ui
   npm install
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

### Running with Docker Compose

To launch the complete containerized stack:
```bash
docker-compose up --build
```
- **Frontend UI**: `http://localhost:80`
- **FastAPI API**: `http://localhost:8000`

---

## Running Benchmarks & Reproducibility

Every experimental result reported in our research is programmatically verifiable:

```bash
# 1. Verify metric reproducibility and held-out KG performance
python test_metric_reproducibility.py

# 2. Run the Prompt Injection Security Benchmark v2 (60 cases)
python run_security_benchmark_v2.py

# 3. Verify closed-form SHAP mathematical faithfulness
python run_shap_pipeline_benchmarks.py

# 4. Run the security benchmark regression test suite
python -m unittest test_security_benchmark_v2_regression.py
```

---

## Research Documentation

SmartHire AI is accompanied by extensive scientific documentation:
- **[`RESEARCH_REPORT.md`](RESEARCH_REPORT.md)**: Full academic research report covering formal mathematical models, agent taxonomy, empirical methodologies, and comprehensive literature comparisons.
- **[`SMARTHIRE_RESEARCH_EVIDENCE_AUDIT.md`](SMARTHIRE_RESEARCH_EVIDENCE_AUDIT.md)**: Forensic evidence audit detailing exact metric proofs, test fixtures, data provenance, and calibration boundaries.
- **[`RESEARCH_PAPER_SECTIONS.md`](RESEARCH_PAPER_SECTIONS.md)**: Ready-to-publish IEEE journal manuscript sections organized according to IEEE Transactions formatting.

---

## Contributing & License

Contributions are welcome! Please submit a pull request or open an issue for feature suggestions or bug reports.

This project is licensed under the **MIT License**.
