"""
Asterisk Setup Script for Phase 2
This script helps set up Asterisk configuration files
"""
import os
import shutil
import platform
import subprocess
import sys


def check_asterisk_installed():
    """Check if Asterisk is installed"""
    try:
        result = subprocess.run(['asterisk', '-V'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Asterisk is installed: {result.stdout.strip()}")
            return True
        else:
            print("✗ Asterisk is not installed")
            return False
    except FileNotFoundError:
        print("✗ Asterisk is not installed or not in PATH")
        return False


def install_asterisk_instructions():
    """Print instructions for installing Asterisk"""
    system = platform.system().lower()
    
    print("\n📋 Asterisk Installation Instructions:")
    print("=" * 50)
    
    if system == "linux":
        print("For Ubuntu/Debian:")
        print("  sudo apt update")
        print("  sudo apt install asterisk")
        print("\nFor CentOS/RHEL:")
        print("  sudo yum install asterisk")
        print("  # or for newer versions:")
        print("  sudo dnf install asterisk")
        
    elif system == "windows":
        print("For Windows:")
        print("  1. Download Asterisk for Windows from:")
        print("     https://www.asterisk.org/downloads/asterisk-all-versions/")
        print("  2. Or use WSL (Windows Subsystem for Linux)")
        print("  3. Or use Docker:")
        print("     docker run -d --name asterisk -p 5060:5060/udp andrius/asterisk")
        
    elif system == "darwin":  # macOS
        print("For macOS:")
        print("  brew install asterisk")
        
    else:
        print("Please check the official Asterisk documentation:")
        print("https://www.asterisk.org/get-started/")


def setup_asterisk_config():
    """Set up Asterisk configuration files"""
    asterisk_dir = "asterisk"
    config_files = ["sip.conf", "extensions.conf"]
    
    print("\n🔧 Setting up Asterisk configuration...")
    
    # Check if asterisk directory exists
    if not os.path.exists(asterisk_dir):
        print(f"✗ Asterisk directory '{asterisk_dir}' not found")
        return False
    
    # Check if config files exist
    missing_files = []
    for config_file in config_files:
        config_path = os.path.join(asterisk_dir, config_file)
        if not os.path.exists(config_path):
            missing_files.append(config_file)
    
    if missing_files:
        print(f"✗ Missing configuration files: {missing_files}")
        return False
    
    print("✓ Configuration files found")
    
    # Determine Asterisk config directory
    system = platform.system().lower()
    if system == "linux":
        asterisk_config_dir = "/etc/asterisk"
    elif system == "windows":
        asterisk_config_dir = "C:\\Program Files\\Asterisk\\etc\\asterisk"
    else:
        asterisk_config_dir = "/etc/asterisk"
    
    print(f"Target Asterisk config directory: {asterisk_config_dir}")
    
    # Check if Asterisk config directory exists
    if not os.path.exists(asterisk_config_dir):
        print(f"✗ Asterisk config directory not found: {asterisk_config_dir}")
        print("Please install Asterisk first or check the installation path")
        return False
    
    # Backup existing files
    print("\n📦 Backing up existing configuration files...")
    for config_file in config_files:
        source_path = os.path.join(asterisk_dir, config_file)
        target_path = os.path.join(asterisk_config_dir, config_file)
        backup_path = os.path.join(asterisk_config_dir, f"{config_file}.backup")
        
        if os.path.exists(target_path):
            try:
                shutil.copy2(target_path, backup_path)
                print(f"✓ Backed up {config_file} to {backup_path}")
            except Exception as e:
                print(f"✗ Failed to backup {config_file}: {e}")
                return False
    
    # Copy new configuration files
    print("\n📋 Installing new configuration files...")
    for config_file in config_files:
        source_path = os.path.join(asterisk_dir, config_file)
        target_path = os.path.join(asterisk_config_dir, config_file)
        
        try:
            shutil.copy2(source_path, target_path)
            print(f"✓ Installed {config_file}")
        except Exception as e:
            print(f"✗ Failed to install {config_file}: {e}")
            return False
    
    return True


def reload_asterisk_config():
    """Reload Asterisk configuration"""
    print("\n🔄 Reloading Asterisk configuration...")
    
    try:
        # Reload SIP configuration
        result1 = subprocess.run(['asterisk', '-rx', 'sip reload'], 
                               capture_output=True, text=True)
        if result1.returncode == 0:
            print("✓ SIP configuration reloaded")
        else:
            print(f"✗ Failed to reload SIP: {result1.stderr}")
            return False
        
        # Reload dialplan
        result2 = subprocess.run(['asterisk', '-rx', 'dialplan reload'], 
                               capture_output=True, text=True)
        if result2.returncode == 0:
            print("✓ Dialplan reloaded")
        else:
            print(f"✗ Failed to reload dialplan: {result2.stderr}")
            return False
        
        return True
        
    except FileNotFoundError:
        print("✗ Asterisk command not found. Please ensure Asterisk is installed and in PATH")
        return False
    except Exception as e:
        print(f"✗ Error reloading configuration: {e}")
        return False


def show_softphone_setup():
    """Show softphone setup instructions"""
    print("\n📱 Softphone Setup Instructions:")
    print("=" * 40)
    print("1. Install a softphone (Zoiper, Linphone, or X-Lite)")
    print("2. Configure the softphone with these settings:")
    print("   - Server: localhost (or your Asterisk server IP)")
    print("   - Username: 1002")
    print("   - Password: softpass123")
    print("   - Domain: localhost")
    print("3. Register the softphone")
    print("4. Call extension 1001 to reach the bot")
    print("\n📞 Test Extensions:")
    print("   - 1001: Bot extension")
    print("   - 1002: Softphone extension")
    print("   - 600: Echo test")


def main():
    """Main setup function"""
    print("🚀 Asterisk Setup for AI Calling Bot - Phase 2")
    print("=" * 60)
    
    # Check if Asterisk is installed
    if not check_asterisk_installed():
        install_asterisk_instructions()
        return 1
    
    # Set up configuration files
    if not setup_asterisk_config():
        print("\n❌ Configuration setup failed")
        return 1
    
    # Reload Asterisk configuration
    if not reload_asterisk_config():
        print("\n❌ Configuration reload failed")
        return 1
    
    # Show softphone setup instructions
    show_softphone_setup()
    
    print("\n✅ Asterisk setup completed successfully!")
    print("\nNext steps:")
    print("1. Install and configure a softphone")
    print("2. Run the SIP voice bot: python -m src.sip_voice_bot")
    print("3. Test the setup by calling extension 1001")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

