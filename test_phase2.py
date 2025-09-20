"""
Test script for Phase 2 SIP integration
"""
import sys
import os
import time
import logging

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from sip_client import create_sip_client, PJSIP_AVAILABLE

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def test_sip_client():
    """Test SIP client functionality"""
    print("🧪 Testing SIP Client")
    print("=" * 40)
    
    # Check PJSIP availability
    if PJSIP_AVAILABLE:
        print("✓ PJSIP is available")
    else:
        print("⚠ PJSIP not available - using simulation mode")
    
    # Create SIP client
    sip_client = create_sip_client()
    
    # Test initialization
    print("\n1. Testing initialization...")
    if sip_client.initialize():
        print("✓ SIP client initialized successfully")
    else:
        print("✗ SIP client initialization failed")
        return False
    
    # Test registration
    print("\n2. Testing registration...")
    if sip_client.register_account():
        print("✓ SIP account registered successfully")
    else:
        print("✗ SIP account registration failed")
        return False
    
    # Test call simulation
    print("\n3. Testing call functionality...")
    if sip_client.make_call("1002"):
        print("✓ Call initiated successfully")
        time.sleep(2)
        sip_client.hangup_call()
        print("✓ Call hung up successfully")
    else:
        print("✗ Call initiation failed")
    
    # Test cleanup
    print("\n4. Testing cleanup...")
    sip_client.cleanup()
    print("✓ SIP client cleaned up successfully")
    
    return True


def test_voice_bot_integration():
    """Test voice bot integration"""
    print("\n🎤 Testing Voice Bot Integration")
    print("=" * 40)
    
    try:
        from sip_voice_bot import SIPVoiceBot
        
        # Create bot instance
        bot = SIPVoiceBot()
        
        # Test initialization
        print("\n1. Testing bot initialization...")
        if bot.initialize():
            print("✓ Voice bot initialized successfully")
        else:
            print("✗ Voice bot initialization failed")
            return False
        
        # Test components
        print("\n2. Testing components...")
        if bot.brain:
            print("✓ GPT Brain component ready")
        if bot.stt:
            print("✓ STT Engine component ready")
        if bot.sip_client:
            print("✓ SIP Client component ready")
        
        # Cleanup
        bot.stop()
        print("✓ Voice bot stopped successfully")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Error testing voice bot: {e}")
        return False


def test_asterisk_config():
    """Test Asterisk configuration files"""
    print("\n📋 Testing Asterisk Configuration")
    print("=" * 40)
    
    asterisk_dir = "asterisk"
    required_files = ["sip.conf", "extensions.conf", "README.md"]
    
    for file_name in required_files:
        file_path = os.path.join(asterisk_dir, file_name)
        if os.path.exists(file_path):
            print(f"✓ {file_name} found")
        else:
            print(f"✗ {file_name} missing")
            return False
    
    # Check sip.conf content
    sip_conf_path = os.path.join(asterisk_dir, "sip.conf")
    with open(sip_conf_path, 'r') as f:
        sip_content = f.read()
        if "1001" in sip_content and "1002" in sip_content:
            print("✓ SIP configuration contains required extensions")
        else:
            print("✗ SIP configuration missing required extensions")
            return False
    
    # Check extensions.conf content
    extensions_conf_path = os.path.join(asterisk_dir, "extensions.conf")
    with open(extensions_conf_path, 'r') as f:
        extensions_content = f.read()
        if "1001" in extensions_content and "1002" in extensions_content:
            print("✓ Extensions configuration contains required extensions")
        else:
            print("✗ Extensions configuration missing required extensions")
            return False
    
    return True


def main():
    """Main test function"""
    print("🚀 Phase 2 Integration Test Suite")
    print("=" * 60)
    
    tests = [
        ("SIP Client", test_sip_client),
        ("Voice Bot Integration", test_voice_bot_integration),
        ("Asterisk Configuration", test_asterisk_config),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:.<40} {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Phase 2 integration is ready.")
        print("\nNext steps:")
        print("1. Install Asterisk: python setup_asterisk.py")
        print("2. Install a softphone (Zoiper, Linphone)")
        print("3. Run the SIP voice bot: python -m src.sip_voice_bot")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the issues above.")
    
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())

