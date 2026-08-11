import os
import chromadb
from google import genai
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from config import GOOGLE_API_KEY


import hashlib

_EMBEDDING_CACHE = {}

class GoogleGenAIEmbeddingFunction(EmbeddingFunction):
    def __init__(self, api_key, model_name="models/gemini-embedding-001"):
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def __call__(self, input: Documents) -> Embeddings:
        results = []
        missing_texts = []
        missing_indices = []

        for idx, text in enumerate(input):
            text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
            if text_hash in _EMBEDDING_CACHE:
                results.append((idx, _EMBEDDING_CACHE[text_hash]))
            else:
                missing_texts.append(text)
                missing_indices.append((idx, text_hash))

        if missing_texts:
            response = self.client.models.embed_content(
                model=self.model_name,
                contents=missing_texts
            )
            for (orig_idx, t_hash), emb in zip(missing_indices, response.embeddings):
                _EMBEDDING_CACHE[t_hash] = emb.values
                results.append((orig_idx, emb.values))

        results.sort(key=lambda x: x[0])
        return [r[1] for r in results]


class ResumeVault:
    def __init__(self, persist_directory="./db/resume_vault"):
        os.makedirs(persist_directory, exist_ok=True)

        self.persist_directory = persist_directory
        self.client = chromadb.PersistentClient(path=persist_directory)

        self.embedding_function = GoogleGenAIEmbeddingFunction(
            api_key=GOOGLE_API_KEY
        )

        self.collection = self.client.get_or_create_collection(
            name="resumes",
            embedding_function=self.embedding_function
        )

    def add_resume(self, resume_text, metadata):
        """Add resume, upload to S3, and store embedding."""

        resume_id = metadata.get("id", os.urandom(4).hex())
        file_name = f"{resume_id}.txt"



        # Gemini Embedding API restricts massive payloads. We truncate the text to the first 8000 characters.
        safe_resume_text = resume_text[:8000] if resume_text else "No content"

        self.collection.add(
            documents=[safe_resume_text],
            metadatas=[metadata],
            ids=[resume_id]
        )

        return resume_id

    def search_similar_resumes(self, query_text, n_results=3):
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

    def get_all_resumes(self):
        return self.collection.get()

    def clear_vault(self):
        self.client.delete_collection(name="resumes")

        self.collection = self.client.get_or_create_collection(
            name="resumes",
            embedding_function=self.embedding_function
        )

        return True


# Global instance
# Global instance
vault = ResumeVault()


from crewai.tools import tool

@tool("search_resume_vault")
def search_resume_vault(query: str) -> str:
    """Useful to search the internal database (Resume Vault) for existing resumes and candidate profiles
    matching a job description or set of skills. Returns top matching candidates and their details."""
    try:
        results = vault.search_similar_resumes(query, n_results=3)
        if not results or not results.get('documents') or not results['documents'][0]:
            return "No candidates found in the Resume Vault matching this query."
        
        output = "--- TOP MATCHING CANDIDATES FROM RESUME VAULT ---\n"
        for i in range(len(results['documents'][0])):
            doc = results['documents'][0][i]
            meta = results['metadatas'][0][i] if results.get('metadatas') else {}
            cand_id = results['ids'][0][i]
            
            output += f"Candidate ID: {cand_id}\n"
            output += f"Name/Email: {meta.get('email', 'Unknown')}\n"
            output += f"Resume Content:\n{doc}\n"
            output += "-" * 40 + "\n"
        return output
    except Exception as e:
        return f"Error searching the Resume Vault: {str(e)}"