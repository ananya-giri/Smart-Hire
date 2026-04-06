import os
import time
from google import genai
from config import GOOGLE_API_KEY

def analyze_video(video_path, prompt):
    """
    Uploads a video to Google GenAI File API and analyzes it with a prompt.
    """
    client = genai.Client(api_key=GOOGLE_API_KEY)
    
    print(f"Uploading file: {video_path}...")
    # Upload the video file
    video_file = client.files.upload(path=video_path)
    print(f"Completed upload: {video_file.uri}")

    # Wait for the file to be processed
    while video_file.state.name == "PROCESSING":
        print('.', end='', flush=True)
        time.sleep(5)
        video_file = client.files.get(name=video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(f"Video processing failed: {video_file.state.name}")

    print("\nAnalyzing video...")
    # Generate content using the video and prompt
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[video_file, prompt]
    )
    
    return response.text

def deepfake_and_teleprompter_analysis(video_path):
    """
    Acts as a Multimodal Integrity Checker using the vision model to detect 
    candidates reading from ChatGPT off-screen or using deepfake avatars.
    """
    forensic_prompt = """
    You are an expert Forensic AI Audio-Visual Analyst. You are tasked with analyzing this async interview video submission.
    Please explicitly analyze the video for the following integrity flags:
    1. Teleprompter / Second Screen Reading: Are the candidate's eyes rhythmically tracking text off-screen? Is there an unnatural lack of direct eye contact?
    2. Deepfake / Avatar Usage: Are there unnatural lip-sync mismatches, robotic head movements, missing blinks, or synthetic facial rendering anomalies (e.g., blurring around the edges)?
    3. Voice Cloning: Does the voice sound unusually robotic, lack natural breathing pauses, or have synthetic artifacts?
    
    Provide a "Video Authenticity Score" from 0 to 100, and explicitly list any RED FLAGS found for deepfakes or teleprompters. Provide a detailed explanation of your visual findings.
    """
    return analyze_video(video_path, forensic_prompt)
