import os

from dotenv import load_dotenv


load_dotenv()


# Audio settings
SAMPLE_RATE = int(os.getenv("SAMPLE_RATE", "16000"))
CHANNELS = 1
RECORD_SECONDS = float(os.getenv("RECORD_SECONDS", "5.0"))
DEVICE_INDEX_IN = os.getenv("DEVICE_INDEX_IN")
DEVICE_INDEX_OUT = os.getenv("DEVICE_INDEX_OUT")


# STT settings
WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "base")
LANGUAGE = os.getenv("LANGUAGE", "en")


# LLM settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are a concise, friendly phone assistant. Ask clarifying questions and help with simple bookings.",
)


# TTS settings
USE_COQUI_TTS = os.getenv("USE_COQUI_TTS", "false").lower() == "true"
TTS_VOICE = os.getenv("TTS_VOICE", "en")


# SIP Settings (Phase 2)
SIP_SERVER_IP = os.getenv("SIP_SERVER_IP", "localhost")
SIP_USERNAME = os.getenv("SIP_USERNAME", "1001")
SIP_PASSWORD = os.getenv("SIP_PASSWORD", "botpass123")
SIP_TARGET_EXTENSION = os.getenv("SIP_TARGET_EXTENSION", "1002")

# UX
PRINT_TRANSCRIPTS = os.getenv("PRINT_TRANSCRIPTS", "true").lower() == "true"
PRINT_BOT_TEXT = os.getenv("PRINT_BOT_TEXT", "true").lower() == "true"


