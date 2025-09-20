"""
Demo script for AI Calling Bot - Phase 1 + Phase 2
"""
import sys
import os
import time

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def demo_phase1():
    """Demo Phase 1 - Local Voice Bot"""
    print("🎤 Phase 1 Demo - Local Voice Bot")
    print("=" * 50)
    
    try:
        from voice_bot import main as voice_bot_main
        print("✓ Phase 1 components loaded successfully")
        print("This would run the local voice bot with mic/speaker")
        print("Run: python -m src.voice_bot")
        return True
    except Exception as e:
        print(f"✗ Phase 1 demo failed: {e}")
        return False

def demo_phase2():
    """Demo Phase 2 - SIP Integration"""
    print("\n📞 Phase 2 Demo - SIP Integration")
    print("=" * 50)
    
    try:
        from sip_voice_bot import SIPVoiceBot
        
        # Create bot instance
        bot = SIPVoiceBot()
        
        # Test initialization
        if bot.initialize():
            print("✓ SIP Voice Bot initialized successfully")
            print("✓ Components ready:")
            print("  - GPT Brain: Ready")
            print("  - STT Engine: Ready") 
            print("  - TTS Engine: Ready")
            print("  - SIP Client: Ready (simulation mode)")
            
            # Cleanup
            bot.stop()
            print("✓ Demo completed successfully")
            return True
        else:
            print("✗ SIP Voice Bot initialization failed")
            return False
            
    except Exception as e:
        print(f"✗ Phase 2 demo failed: {e}")
        return False

def demo_asterisk_setup():
    """Demo Asterisk setup"""
    print("\n🔧 Asterisk Setup Demo")
    print("=" * 50)
    
    asterisk_dir = "asterisk"
    config_files = ["sip.conf", "extensions.conf"]
    
    print("Configuration files:")
    for config_file in config_files:
        file_path = os.path.join(asterisk_dir, config_file)
        if os.path.exists(file_path):
            print(f"✓ {config_file}")
        else:
            print(f"✗ {config_file}")
            return False
    
    print("\nSIP Extensions configured:")
    print("  - 1001: Bot extension (password: botpass123)")
    print("  - 1002: Softphone extension (password: softpass123)")
    print("  - 600: Echo test")
    
    print("\nTo setup Asterisk:")
    print("  python setup_asterisk.py")
    
    return True

def main():
    """Main demo function"""
    print("🚀 AI Calling Bot - Phase 1 + Phase 2 Demo")
    print("=" * 60)
    
    demos = [
        ("Phase 1 - Local Voice Bot", demo_phase1),
        ("Phase 2 - SIP Integration", demo_phase2),
        ("Asterisk Setup", demo_asterisk_setup),
    ]
    
    results = []
    
    for demo_name, demo_func in demos:
        try:
            result = demo_func()
            results.append((demo_name, result))
        except Exception as e:
            print(f"✗ {demo_name} failed with exception: {e}")
            results.append((demo_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("📊 DEMO SUMMARY")
    print("="*60)
    
    passed = 0
    total = len(results)
    
    for demo_name, result in results:
        status = "✓ READY" if result else "✗ ISSUES"
        print(f"{demo_name:.<40} {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} demos ready")
    
    if passed == total:
        print("\n🎉 All phases are ready!")
        print("\n📋 Next Steps:")
        print("1. Phase 1: python -m src.voice_bot")
        print("2. Phase 2: python -m src.sip_voice_bot")
        print("3. Setup Asterisk: python setup_asterisk.py")
        print("4. Install softphone (Zoiper, Linphone)")
        print("5. Test calls between extensions")
    else:
        print(f"\n⚠️  {total - passed} demo(s) have issues. Check the output above.")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())

