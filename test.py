import sys
import os
from main import run_recruitment_flow

print("Starting test of CrewAI with gemini-flash-lite-latest...")
try:
    res = run_recruitment_flow(
        "Candidate has 5 years React experience.", 
        "Looking for a React developer."
    )
    print("Successfully ran recruitment flow without errors!")
except Exception as e:
    print(f"Encountered an exception: {e}")
