import networkx as nx
from typing import Optional, Union, List
from crewai.tools import tool

# Common tech alias mappings for robust normalization
SKILL_ALIASES = {
    "reactjs": "React",
    "react.js": "React",
    "nextjs": "Next.js",
    "next": "Next.js",
    "vuejs": "Vue",
    "vue.js": "Vue",
    "angularjs": "Angular",
    "nodejs": "Node.js",
    "node": "Node.js",
    "expressjs": "Express",
    "express.js": "Express",
    "fast-api": "FastAPI",
    "ts": "TypeScript",
    "typescript": "TypeScript",
    "js": "JavaScript",
    "javascript": "JavaScript",
    "py": "Python",
    "python3": "Python",
    "golang": "Go",
    "k8s": "Kubernetes",
    "k8": "Kubernetes",
    "docker-compose": "Docker",
    "amazon web services": "AWS",
    "google cloud": "GCP",
    "google cloud platform": "GCP",
    "microsoft azure": "Azure",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "mongo": "MongoDB",
    "mongodb": "MongoDB",
    "sklearn": "Scikit-Learn",
    "scikit_learn": "Scikit-Learn",
    "scikitlearn": "Scikit-Learn",
    "pytorch": "PyTorch",
    "tf": "TensorFlow",
    "tensorflow": "TensorFlow",
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",
    "genai": "Generative AI",
    "gen-ai": "Generative AI",
    "generative ai": "Generative AI",
    "llm": "LLMs",
    "llms": "LLMs",
    "ci/cd": "CI/CD",
    "cicd": "CI/CD",
    "github actions": "GitHub Actions",
    "gh actions": "GitHub Actions",
    "restful": "REST",
    "rest api": "REST",
    "rest apis": "REST",
    "graph-ql": "GraphQL",
    "graphql": "GraphQL"
}

def build_tech_graph() -> nx.Graph:
    G = nx.Graph()
    
    # Domains & Frontend
    G.add_edge("Frontend", "JavaScript", weight=1)
    G.add_edge("Frontend", "TypeScript", weight=1)
    G.add_edge("JavaScript", "TypeScript", weight=1)
    G.add_edge("JavaScript", "React", weight=1)
    G.add_edge("TypeScript", "React", weight=1)
    G.add_edge("React", "Next.js", weight=1)
    G.add_edge("JavaScript", "Vue", weight=1)
    G.add_edge("Vue", "Nuxt", weight=1)
    G.add_edge("TypeScript", "Angular", weight=1)
    G.add_edge("Frontend", "HTML5", weight=1)
    G.add_edge("Frontend", "CSS3", weight=1)
    G.add_edge("CSS3", "TailwindCSS", weight=1)
    G.add_edge("React", "Redux", weight=1)
    G.add_edge("React", "Zustand", weight=1)
    
    # Backend & Languages
    G.add_edge("Backend", "Python", weight=1)
    G.add_edge("Backend", "Node.js", weight=1)
    G.add_edge("Backend", "Java", weight=1)
    G.add_edge("Backend", "Go", weight=1)
    G.add_edge("Backend", "C++", weight=1)
    G.add_edge("Backend", "Rust", weight=1)
    G.add_edge("Python", "Django", weight=1)
    G.add_edge("Python", "FastAPI", weight=1)
    G.add_edge("Python", "Flask", weight=1)
    G.add_edge("Node.js", "Express", weight=1)
    G.add_edge("Node.js", "NestJS", weight=1)
    G.add_edge("Java", "Spring Boot", weight=1)
    G.add_edge("Backend", "REST", weight=1)
    G.add_edge("Backend", "GraphQL", weight=1)
    G.add_edge("Backend", "gRPC", weight=1)
    G.add_edge("Backend", "Microservices", weight=1)
    
    # Cloud, Infrastructure & DevOps
    G.add_edge("Cloud", "AWS", weight=1)
    G.add_edge("Cloud", "GCP", weight=1)
    G.add_edge("Cloud", "Azure", weight=1)
    G.add_edge("AWS", "EC2", weight=1)
    G.add_edge("AWS", "S3", weight=1)
    G.add_edge("AWS", "Lambda", weight=1)
    G.add_edge("DevOps", "Docker", weight=1)
    G.add_edge("DevOps", "Kubernetes", weight=1)
    G.add_edge("Docker", "Kubernetes", weight=1)
    G.add_edge("DevOps", "Terraform", weight=1)
    G.add_edge("DevOps", "CI/CD", weight=1)
    G.add_edge("CI/CD", "GitHub Actions", weight=1)
    G.add_edge("CI/CD", "Jenkins", weight=1)
    G.add_edge("DevOps", "Linux", weight=1)
    G.add_edge("DevOps", "Git", weight=1)
    
    # Databases & Storage
    G.add_edge("Database", "SQL", weight=1)
    G.add_edge("SQL", "PostgreSQL", weight=1)
    G.add_edge("SQL", "MySQL", weight=1)
    G.add_edge("Database", "MongoDB", weight=1)
    G.add_edge("Database", "Redis", weight=1)
    G.add_edge("Database", "Snowflake", weight=1)
    G.add_edge("Backend", "Database", weight=1)
    G.add_edge("Backend", "Kafka", weight=1)
    G.add_edge("Backend", "RabbitMQ", weight=1)
    
    # Data & Machine Learning / AI
    G.add_edge("Python", "Machine Learning", weight=1)
    G.add_edge("Artificial Intelligence", "Machine Learning", weight=1)
    G.add_edge("Machine Learning", "Deep Learning", weight=1)
    G.add_edge("Machine Learning", "PyTorch", weight=1)
    G.add_edge("Machine Learning", "TensorFlow", weight=1)
    G.add_edge("Machine Learning", "Scikit-Learn", weight=1)
    G.add_edge("Machine Learning", "Pandas", weight=1)
    G.add_edge("Machine Learning", "NumPy", weight=1)
    G.add_edge("Deep Learning", "NLP", weight=1)
    G.add_edge("Deep Learning", "Computer Vision", weight=1)
    G.add_edge("NLP", "LLMs", weight=1)
    G.add_edge("LLMs", "Generative AI", weight=1)
    G.add_edge("Data Engineering", "SQL", weight=1)
    G.add_edge("Data Engineering", "Spark", weight=1)
    G.add_edge("Data Engineering", "Airflow", weight=1)
    G.add_edge("Data Engineering", "Python", weight=1)
    
    # Cross-domain bridges
    G.add_edge("Frontend", "Backend", weight=2)
    G.add_edge("Backend", "Cloud", weight=1)
    G.add_edge("Cloud", "DevOps", weight=1)
    G.add_edge("Backend", "Data Engineering", weight=2)

    return G

# Singleton graph instance initialized at module load
_GLOBAL_TECH_GRAPH = build_tech_graph()

def _normalize_skill_name(skill_str: str, graph_nodes: set) -> str:
    """Normalizes skill string using alias mapping and case-insensitive matching."""
    s = skill_str.strip()
    s_lower = s.lower().replace("-", " ").replace("_", " ")
    
    # Check direct aliases
    if s.lower() in SKILL_ALIASES:
        return SKILL_ALIASES[s.lower()]
    if s_lower in SKILL_ALIASES:
        return SKILL_ALIASES[s_lower]
        
    # Check exact case match with graph
    for node in graph_nodes:
        if node.lower() == s.lower() or node.lower() == s_lower:
            return node
            
    return s

@tool("semantic_skill_graph_matcher")
def semantic_skill_graph_matcher(required_skill: str, candidate_skills_csv: str) -> str:
    """Useful to mathematically measure the distance between a required job skill and a candidate's actual skills using a Neuro-Symbolic Knowledge Graph.
    Pass the required_skill and a comma-separated list of candidate_skills. 
    It returns if there is a latent mathematical semantic connection."""
    if not required_skill or not str(required_skill).strip():
        return "Error: required_skill cannot be empty."

    G = _GLOBAL_TECH_GRAPH
    graph_nodes = set(G.nodes)
    
    req_clean = str(required_skill).strip()
    req_mapped = _normalize_skill_name(req_clean, graph_nodes)
    
    # Parse candidate skills
    if not candidate_skills_csv:
        candidate_skills_list = []
    elif isinstance(candidate_skills_csv, list):
        candidate_skills_list = [str(x).strip() for x in candidate_skills_csv if str(x).strip()]
    else:
        candidate_skills_list = [s.strip() for s in str(candidate_skills_csv).replace(";", ",").replace("\n", ",").split(",") if s.strip()]
    
    if not candidate_skills_list:
        return f"No candidate skills provided. Cannot match '{req_clean}'."

    # Check graph for the requirement
    if req_mapped not in G:
        # Check if candidate has an exact string match despite not being in graph
        for c_skill in candidate_skills_list:
            if c_skill.lower() == req_clean.lower():
                return f"Exact Explicit Match found for '{req_clean}' (textual match)."
        return f"Skill '{req_clean}' is specialized or not mapped in standard generic graph. LLM must use native contextual reasoning."
    
    closest_skill = None
    min_dist = float('inf')
    
    for skill in candidate_skills_list:
        skill_mapped = _normalize_skill_name(skill, graph_nodes)
        if skill_mapped in G:
            try:
                dist = nx.shortest_path_length(G, source=req_mapped, target=skill_mapped)
                if dist < min_dist:
                    min_dist = dist
                    closest_skill = skill_mapped
            except nx.NetworkXNoPath:
                pass
        elif skill.lower() == req_clean.lower():
            min_dist = 0
            closest_skill = req_mapped
                
    if min_dist == 0:
        return f"Exact Explicit Match found for '{req_clean}'."
    elif min_dist <= 2:
        return f"Latent Neuro-Symbolic match found: Candidate lacks explicit '{req_clean}', but has '{closest_skill}' which is mathematically related in the knowledge graph (Graph Path Distance: {min_dist}). Approve skill."
    elif min_dist <= 3:
        return f"Moderate Domain proximity found between '{req_clean}' and candidate's skill '{closest_skill}' (Graph Path Distance: {min_dist}). Partially transferable skill."
    else:
        return f"No close semantic connection found in the skill network for '{req_clean}'. Flag as a gap."

def get_kg_tool():
    return semantic_skill_graph_matcher

