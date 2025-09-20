# 🚀 AI Calling Bot - Complete User Guide

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Installation & Setup](#installation--setup)
3. [Running Options](#running-options)
4. [Configuration Options](#configuration-options)
5. [Different Modes & What They Do](#different-modes--what-they-do)
6. [Testing & Validation](#testing--validation)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Usage](#advanced-usage)

---

## 🎯 Project Overview

This AI Calling Bot project implements **Phase 1** and **Phase 2** of a complete voice bot system:

- **Phase 1**: Local voice bot (STT → GPT → TTS) using microphone and speakers
- **Phase 2**: SIP integration with Asterisk PBX for real call simulation
- **Integrated**: Combined SIP voice bot ready for production testing

### 🏗️ Architecture
```
Phase 1: Microphone → Whisper (STT) → OpenAI GPT → gTTS → Speakers
Phase 2: SIP Call → Asterisk → Bot Engine → Asterisk → SIP Call
```

---

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.10+**
- **FFmpeg** (for audio playback)
- **OpenAI API Key**
- **Windows 10/11** (project optimized for Windows)

### Quick Setup
```bash
# 1. Navigate to project directory
cd call-ai-

# 2. Create virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with your OpenAI API key
# (Copy from .env.example or create new)
```

### Environment File (.env)
```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4o-mini

# System Prompt
SYSTEM_PROMPT=You are a concise, friendly phone assistant. Ask clarifying questions and help with simple bookings.

# Audio Settings
SAMPLE_RATE=16000
RECORD_SECONDS=5.0
DEVICE_INDEX_IN=1
DEVICE_INDEX_OUT=3

# STT Settings
WHISPER_MODEL_SIZE=base
LANGUAGE=en

# TTS Settings
USE_COQUI_TTS=false
TTS_VOICE=en

# SIP Settings (Phase 2)
SIP_SERVER_IP=localhost
SIP_USERNAME=1001
SIP_PASSWORD=botpass123
SIP_TARGET_EXTENSION=1002

# UX Settings
PRINT_TRANSCRIPTS=true
PRINT_BOT_TEXT=true
```

---

## 🚀 Running Options

### 1. **Phase 1 - Local Voice Bot**
```bash
python -m src.voice_bot
```
**What it does:**
- Uses your microphone and speakers
- Press Enter → speak → bot responds
- Perfect for testing the AI pipeline
- No network required (except OpenAI API)

**Interaction:**
- Press `Enter` to start recording
- Speak for up to 5 seconds
- Bot processes and responds via speakers
- Type `quit` to exit

### 2. **Phase 2 - SIP Voice Bot**
```bash
python -m src.sip_voice_bot
```
**What it does:**
- Connects to Asterisk PBX via SIP
- Simulates real phone calls
- Uses SIP extensions (1001 for bot, 1002 for softphone)
- Currently runs in simulation mode

**Commands:**
- `call <number>` - Make a call to extension
- `answer` - Answer incoming call
- `hangup` - Hang up current call
- `quit` - Exit the bot

### 3. **Simple Voice Bot (Configuration Check)**
```bash
python simple_voice_bot.py
```
**What it does:**
- Checks if OpenAI API key is configured
- Shows current configuration
- Validates setup without running full bot
- Good for troubleshooting

### 4. **Demo Mode**
```bash
python demo.py
```
**What it does:**
- Tests all components
- Shows what's working and what's not
- Validates Phase 1 and Phase 2 integration
- Provides status report

### 5. **Testing Suite**
```bash
# Test Phase 2 integration
python test_phase2.py

# Test imports and dependencies
python test_imports.py

# List available audio devices
python -m src.tools.list_devices
```

### 6. **Asterisk Setup**
```bash
python setup_asterisk.py
```
**What it does:**
- Automatically configures Asterisk
- Sets up SIP extensions
- Provides installation instructions
- Configures call routing

---

## ⚙️ Configuration Options

### Audio Configuration
| Setting | Default | Effect | Options |
|---------|---------|--------|---------|
| `SAMPLE_RATE` | 16000 | Audio quality | 8000, 16000, 44100 |
| `RECORD_SECONDS` | 5.0 | Recording duration | 1.0-10.0 |
| `DEVICE_INDEX_IN` | 1 | Input microphone | Use `list_devices` to find |
| `DEVICE_INDEX_OUT` | 3 | Output speakers | Use `list_devices` to find |

### Speech-to-Text (STT)
| Setting | Default | Effect | Options |
|---------|---------|--------|---------|
| `WHISPER_MODEL_SIZE` | base | Accuracy vs Speed | tiny, small, base, medium, large |
| `LANGUAGE` | en | Recognition language | en, es, fr, de, etc. |

### Text-to-Speech (TTS)
| Setting | Default | Effect | Options |
|---------|---------|--------|---------|
| `USE_COQUI_TTS` | false | Offline TTS | true/false |
| `TTS_VOICE` | en | Voice language | en, es, fr, de, etc. |

### AI Brain (GPT)
| Setting | Default | Effect | Options |
|---------|---------|--------|---------|
| `OPENAI_MODEL` | gpt-4o-mini | AI model | gpt-4o-mini, gpt-4, gpt-3.5-turbo |
| `SYSTEM_PROMPT` | "You are a concise..." | Bot personality | Any text prompt |

### SIP Configuration (Phase 2)
| Setting | Default | Effect | Options |
|---------|---------|--------|---------|
| `SIP_SERVER_IP` | localhost | Asterisk server | IP address or hostname |
| `SIP_USERNAME` | 1001 | Bot extension | Any SIP username |
| `SIP_PASSWORD` | botpass123 | SIP password | Any password |
| `SIP_TARGET_EXTENSION` | 1002 | Default call target | Any extension number |

### User Experience
| Setting | Default | Effect | Options |
|---------|---------|--------|---------|
| `PRINT_TRANSCRIPTS` | true | Show speech text | true/false |
| `PRINT_BOT_TEXT` | true | Show bot responses | true/false |

---

## 🎛️ Different Modes & What They Do

### Mode 1: **Local Testing Mode**
**Command:** `python -m src.voice_bot`
**Use Case:** Development, testing AI responses
**Requirements:** Microphone, speakers, OpenAI API
**Network:** Internet for OpenAI API only
**Audio Flow:** Mic → Bot → Speakers

### Mode 2: **SIP Simulation Mode**
**Command:** `python -m src.sip_voice_bot`
**Use Case:** Testing SIP integration without real Asterisk
**Requirements:** All Phase 1 components
**Network:** Internet for OpenAI API
**Audio Flow:** Simulated SIP → Bot → Simulated SIP

### Mode 3: **Real SIP Mode** (Requires Asterisk)
**Command:** `python -m src.sip_voice_bot` (with Asterisk running)
**Use Case:** Real call testing with softphone
**Requirements:** Asterisk PBX, softphone, all bot components
**Network:** Local network + Internet for OpenAI API
**Audio Flow:** Softphone → Asterisk → Bot → Asterisk → Softphone

### Mode 4: **Configuration Check Mode**
**Command:** `python simple_voice_bot.py`
**Use Case:** Troubleshooting, setup validation
**Requirements:** None (just checks config)
**Network:** None
**Audio Flow:** None

### Mode 5: **Demo/Test Mode**
**Command:** `python demo.py` or `python test_phase2.py`
**Use Case:** Validation, demonstration
**Requirements:** All dependencies installed
**Network:** Internet for OpenAI API
**Audio Flow:** Test components only

---

## 🧪 Testing & Validation

### Quick Health Check
```bash
# 1. Test all imports
python test_imports.py

# 2. Test Phase 2 integration
python test_phase2.py

# 3. Run demo
python demo.py
```

### Audio Device Testing
```bash
# List available audio devices
python -m src.tools.list_devices

# Test with specific device
# Edit .env: DEVICE_INDEX_IN=1, DEVICE_INDEX_OUT=3
python -m src.voice_bot
```

### SIP Testing (Phase 2)
```bash
# 1. Setup Asterisk
python setup_asterisk.py

# 2. Install softphone (Zoiper/Linphone)
# 3. Configure softphone:
#    - Server: localhost
#    - Username: 1002
#    - Password: softpass123
# 4. Run SIP bot
python -m src.sip_voice_bot
# 5. Call extension 1001 from softphone
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **"No module named 'soundfile'"**
```bash
pip install soundfile pygame
```

#### 2. **"OPENAI_API_KEY is missing"**
- Check `.env` file exists
- Verify API key is correct
- Run `python simple_voice_bot.py` to validate

#### 3. **"No audio devices found"**
```bash
python -m src.tools.list_devices
# Update DEVICE_INDEX_IN and DEVICE_INDEX_OUT in .env
```

#### 4. **"STT is slow"**
- Change `WHISPER_MODEL_SIZE` to `tiny` or `small`
- Edit `src/stt.py` for model selection

#### 5. **"TTS playback fails"**
- Install FFmpeg and add to PATH
- Try different audio players
- Check `DEVICE_INDEX_OUT` setting

#### 6. **"SIP client not working"**
- Install PJSIP: `pip install pjsua2`
- Or use simulation mode (default)
- Check Asterisk is running

### Performance Optimization

#### For Faster STT:
```bash
# In .env
WHISPER_MODEL_SIZE=tiny  # or small
```

#### For Better STT Accuracy:
```bash
# In .env
WHISPER_MODEL_SIZE=medium  # or large
```

#### For Offline TTS:
```bash
# In .env
USE_COQUI_TTS=true
# Then: pip install TTS
```

---

## 🚀 Advanced Usage

### Custom System Prompts
Edit `.env`:
```bash
SYSTEM_PROMPT=You are a customer service representative for a restaurant. Help customers with reservations, menu questions, and orders. Be friendly and professional.
```

### Multi-language Support
```bash
# For Spanish
LANGUAGE=es
TTS_VOICE=es
SYSTEM_PROMPT=Eres un asistente telefónico amigable. Ayuda con reservas y preguntas.

# For French
LANGUAGE=fr
TTS_VOICE=fr
SYSTEM_PROMPT=Vous êtes un assistant téléphonique amical. Aidez avec les réservations et questions.
```

### Custom Audio Settings
```bash
# High quality audio
SAMPLE_RATE=44100
RECORD_SECONDS=10.0

# Fast processing
SAMPLE_RATE=8000
RECORD_SECONDS=3.0
```

### SIP Server Configuration
```bash
# For remote Asterisk server
SIP_SERVER_IP=192.168.1.100
SIP_USERNAME=bot001
SIP_PASSWORD=secure_password123
```

### Production Deployment
1. **Use Coqui TTS** for offline operation
2. **Set up real Asterisk** server
3. **Configure SIP trunks** for external calls
4. **Add logging and monitoring**
5. **Implement call recording**

---

## 📊 Project Status

### ✅ Completed Features
- [x] Phase 1: Complete STT → GPT → TTS pipeline
- [x] Phase 2: SIP client integration
- [x] Asterisk configuration
- [x] Testing suite
- [x] Setup automation
- [x] Multi-platform support
- [x] Configuration management

### 🔄 Current Limitations
- SIP integration runs in simulation mode (PJSIP optional)
- No real-time audio streaming (turn-based)
- No call recording
- No advanced call management

### 🎯 Next Steps (Phase 3)
- Real SIP trunk integration
- Call recording and logging
- Advanced call management
- Production deployment tools

---

## 📞 Support & Resources

### Documentation
- `README.md` - Basic setup and usage
- `COMPLETE_GUIDE.md` - This comprehensive guide
- `phases.md` - Project roadmap and phases
- `asterisk/README.md` - Asterisk-specific setup

### Configuration Files
- `.env` - Main configuration
- `src/config.py` - Python configuration
- `asterisk/sip.conf` - SIP configuration
- `asterisk/extensions.conf` - Call routing

### Testing Scripts
- `test_imports.py` - Dependency testing
- `test_phase2.py` - Integration testing
- `demo.py` - Component demonstration
- `setup_asterisk.py` - Asterisk automation

---

**🎉 You're now ready to use the AI Calling Bot! Start with `python demo.py` to see what's working, then choose your preferred mode based on your needs.**
