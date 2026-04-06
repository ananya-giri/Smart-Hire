import requests
from crewai.tools import tool

@tool("analyze_github_profile")
def analyze_github_profile(github_username: str) -> str:
    """Useful to fetch and analyze a candidate's real public GitHub repositories and programming languages.
    Requires the exact github username. Do not pass full URLs, only the username."""
    try:
        url = f"https://api.github.com/users/{github_username}/repos?sort=updated&per_page=5"
        # We use a user-agent to avoid API blocking
        headers = {'User-Agent': 'SmartHire-Recruitment-AI'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            return f"GitHub profile '{github_username}' not found. Candidate may not have public repositories."
        if response.status_code != 200:
            return f"Failed to fetch GitHub profile for '{github_username}'. Status Code: {response.status_code}. Rate limit may be exceeded."
            
        repos = response.json()
        if not repos:
            return f"GitHub profile '{github_username}' has no public repositories."
            
        analysis = f"GitHub Portfolio Analysis for '{github_username}':\n"
        for repo in repos:
            name = repo.get("name", "Unknown")
            language = repo.get("language", "Unknown")
            description = repo.get("description", "No description")
            stars = repo.get("stargazers_count", 0)
            
            analysis += f"- Repo: {name} | Language: {language} | Stars: {stars}\n"
            if description:
                analysis += f"  Desc: {description}\n"
            
        return analysis
    except Exception as e:
         return f"Error connecting to GitHub API: {str(e)}"

def get_github_tool():
    return analyze_github_profile
