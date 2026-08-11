import networkx as nx
from crewai.tools import tool

def build_tech_graph():
    G = nx.Graph()
    # High-level Domains
    G.add_edge("Frontend", "React", weight=1)
    G.add_edge("React", "Next.js", weight=1)
    G.add_edge("Frontend", "Vue", weight=1)
    G.add_edge("Frontend", "Angular", weight=1)
    
    # Backend
    G.add_edge("Backend", "Python", weight=1)
    G.add_edge("Backend", "Node.js", weight=1)
    G.add_edge("Python", "Django", weight=1)
    G.add_edge("Python", "FastAPI", weight=1)
    G.add_edge("Node.js", "Express", weight=1)
    
    # Cloud & DevOps
    G.add_edge("Cloud", "AWS", weight=1)
    G.add_edge("Cloud", "GCP", weight=1)
    G.add_edge("AWS", "EC2", weight=1)
    G.add_edge("AWS", "S3", weight=1)
    G.add_edge("DevOps", "Docker", weight=1)
    G.add_edge("DevOps", "Kubernetes", weight=1)
    G.add_edge("Docker", "Kubernetes", weight=1)
    
    # Data & Machine Learning
    G.add_edge("Python", "Machine Learning", weight=2)
    G.add_edge("Machine Learning", "PyTorch", weight=1)
    G.add_edge("Machine Learning", "TensorFlow", weight=1)
    G.add_edge("Machine Learning", "Scikit-Learn", weight=1)
    G.add_edge("Data Engineering", "SQL", weight=1)
    G.add_edge("Data Engineering", "Spark", weight=1)
    G.add_edge("Data Engineering", "Python", weight=1)
    
    return G

# Singleton graph instance initialized at module load
_GLOBAL_TECH_GRAPH = build_tech_graph()

@tool("semantic_skill_graph_matcher")
def semantic_skill_graph_matcher(required_skill: str, candidate_skills_csv: str) -> str:
    """Useful to mathematically measure the distance between a required job skill and a candidate's actual skills using a Neuro-Symbolic Knowledge Graph.
    Pass the required_skill and a comma-separated list of candidate_skills. 
    It returns if there is a latent mathematical semantic connection."""
    G = _GLOBAL_TECH_GRAPH
    
    req = required_skill.strip()
    # Attempt basic normalization matching the graph nodes (which are largely capitalized/title case)
    req_mapped = next((node for node in G.nodes if node.lower() == req.lower()), req)
    
    candidate_skills = [s.strip() for s in candidate_skills_csv.split(",")]
    
    # Check graph for the requirement
    if req_mapped not in G:
        return f"Skill '{req}' is too niche or not mapped in standard generic graph. LLM must use native contextual reasoning."
    
    closest_skill = None
    min_dist = float('inf')
    
    for skill in candidate_skills:
        skill_mapped = next((node for node in G.nodes if node.lower() == skill.lower()), skill)
        if skill_mapped in G:
            try:
                dist = nx.shortest_path_length(G, source=req_mapped, target=skill_mapped)
                if dist < min_dist:
                    min_dist = dist
                    closest_skill = skill_mapped
            except nx.NetworkXNoPath:
                pass
                
    if min_dist == 0:
        return f"Exact Explicit Match found for '{req}'."
    elif min_dist <= 2:
        return f"Latent Neuro-Symbolic match found: Candidate lacks explicit '{req}', but has '{closest_skill}' which is mathematically related in the knowledge graph (Graph Path Distance: {min_dist}). Approve skill."
    else:
        return f"No close semantic connection found in the skill network for '{req}'. Flag as a gap."

def get_kg_tool():
    return semantic_skill_graph_matcher
