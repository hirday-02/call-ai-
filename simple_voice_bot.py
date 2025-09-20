#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Simple configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a concise, friendly phone assistant. Ask clarifying questions and help with simple bookings.")

def main():
    print("🎤 Simple Voice Bot")
    print("=" * 50)
    
    # Check if OpenAI API key is set
    if not OPENAI_API_KEY or OPENAI_API_KEY == "REPLACE_ME":
        print("❌ Error: OPENAI_API_KEY is missing!")
        print("Please set your OpenAI API key in the .env file")
        return 1
    
    print(f"✅ OpenAI API Key: {OPENAI_API_KEY[:20]}...")
    print(f"✅ Model: {OPENAI_MODEL}")
    print(f"✅ System Prompt: {SYSTEM_PROMPT}")
    
    print("\n🎯 Voice Bot is ready!")
    print("This is a simplified version that shows the configuration.")
    print("To run the full voice bot with speech recognition and TTS,")
    print("you'll need to install additional packages:")
    print("- faster-whisper (for speech-to-text)")
    print("- sounddevice (for audio recording)")
    print("- numpy (for audio processing)")
    print("- gtts (for text-to-speech)")
    print("- soundfile (for audio file handling)")
    
    print("\nTo install these packages, run:")
    print("pip install faster-whisper sounddevice numpy gtts soundfile")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
