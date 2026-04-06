from tools.rag_processor import vault

try:
    print("Attempting to save to vault...")
    vault.add_resume("This is a sample resume text.", {"role": "Engineer", "source": "test.pdf", "ai_score": 85, "timestamp": 1234.5})
    print("Save completed!")
    print("Current Vault contents Count:", len(vault.get_all_resumes()['documents']))
except Exception as e:
    import traceback
    traceback.print_exc()
