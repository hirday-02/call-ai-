#!/usr/bin/env python3

print("Testing imports...")

try:
    from dotenv import load_dotenv
    print("✓ dotenv imported successfully")
except ImportError as e:
    print(f"✗ dotenv import failed: {e}")

try:
    from openai import OpenAI
    print("✓ openai imported successfully")
except ImportError as e:
    print(f"✗ openai import failed: {e}")

try:
    import numpy as np
    print("✓ numpy imported successfully")
except ImportError as e:
    print(f"✗ numpy import failed: {e}")

try:
    import sounddevice as sd
    print("✓ sounddevice imported successfully")
except ImportError as e:
    print(f"✗ sounddevice import failed: {e}")

try:
    from faster_whisper import WhisperModel
    print("✓ faster-whisper imported successfully")
except ImportError as e:
    print(f"✗ faster-whisper import failed: {e}")

try:
    from gtts import gTTS
    print("✓ gtts imported successfully")
except ImportError as e:
    print(f"✗ gtts import failed: {e}")

try:
    import soundfile
    print("✓ soundfile imported successfully")
except ImportError as e:
    print(f"✗ soundfile import failed: {e}")

print("Import test completed.")
