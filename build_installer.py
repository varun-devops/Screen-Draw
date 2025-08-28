"""
Build script for creating a Windows installer for WebtroopsScreen Draw

This script uses PyInstaller to create a standalone executable and
then uses Inno Setup to create a Windows installer.

Requirements:
- PyInstaller
- Inno Setup (must be installed on the system)
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Configuration
APP_NAME = "WebtroopsScreen Draw"
APP_VERSION = "1.0.0"
MAIN_SCRIPT = "WebTroopScreenDraw.py"
ICON_FILE = "assets/icon.ico"
OUTPUT_DIR = "dist"

def clean_output_directories():
    """Clean build and dist directories"""
    print("Cleaning output directories...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    print("Output directories cleaned")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable with PyInstaller...")
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        f"--icon={ICON_FILE}",
        f"--name={APP_NAME}",
        "--clean",
        MAIN_SCRIPT
    ]
    subprocess.run(cmd, check=True)
    print("Executable build complete")

def create_inno_setup_script():
    """Create the Inno Setup script"""
    print("Creating Inno Setup script...")
    
    script_content = f"""
#define MyAppName "{APP_NAME}"
#define MyAppVersion "{APP_VERSION}"
#define MyAppPublisher "WebTroop"
#define MyAppURL "https://github.com/YourUsername/WebTroopScreenDraw"
#define MyAppExeName "{APP_NAME}.exe"

[Setup]
AppId={{{{F9D7B4E0-8C36-4F3A-B1B8-E9F8E9E9E9E9}}}}
AppName={{#MyAppName}}
AppVersion={{#MyAppVersion}}
AppPublisher={{#MyAppPublisher}}
AppPublisherURL={{#MyAppURL}}
AppSupportURL={{#MyAppURL}}
AppUpdatesURL={{#MyAppURL}}
DefaultDirName={{autopf}}\\{{#MyAppPublisher}}\\{{#MyAppName}}
DefaultGroupName={{#MyAppName}}
DisableProgramGroupPage=yes
OutputBaseFilename={{#MyAppName}}_Setup_{{#MyAppVersion}}
; Removed SetupIconFile to avoid icon size issue
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked
Name: "startmenuicon"; Description: "Create Start Menu shortcuts"; GroupDescription: "{{cm:AdditionalIcons}}";
Name: "startupicon"; Description: "Start automatically with Windows"; GroupDescription: "Startup";
Name: "registerhotkey"; Description: "Register global hotkey (F9)"; GroupDescription: "Options";

[Files]
Source: "dist\\{APP_NAME}.exe"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "assets\\*"; DestDir: "{{app}}\\assets"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{{autoprograms}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"
Name: "{{autodesktop}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: desktopicon
Name: "{{commonstartup}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: startupicon

[Run]
Filename: "{{app}}\\{{#MyAppExeName}}"; Description: "{{cm:LaunchProgram,{{#StringChange(MyAppName, '&', '&&')}}}}"; Flags: nowait postinstall skipifsilent
"""

    with open("installer_script.iss", "w") as f:
        f.write(script_content)
    
    print("Inno Setup script created")

def build_installer():
    """Build the installer using Inno Setup"""
    print("Building installer with Inno Setup...")
    
    # Path to the Inno Setup Compiler (iscc.exe)
    iscc_path = "D:\\Inno Setup 6\\ISCC.exe"
    
    # Check if Inno Setup is installed
    if not os.path.exists(iscc_path):
        print(f"Error: Inno Setup not found at {iscc_path}")
        print("Please check the installation path and try again.")
        return False
    
    # Run the Inno Setup Compiler
    print(f"Running Inno Setup compiler from: {iscc_path}")
    subprocess.run([iscc_path, "installer_script.iss"], check=True)
    
    print("Installer build complete")
    return True

def main():
    """Main build process"""
    try:
        # Ensure we're in the right directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        print(f"Building {APP_NAME} v{APP_VERSION}")
        
        # Step 1: Clean output directories
        clean_output_directories()
        
        # Step 2: Build the executable
        build_executable()
        
        # Step 3: Create Inno Setup script
        create_inno_setup_script()
        
        # Step 4: Build the installer
        success = build_installer()
        
        if success:
            print(f"\nBuild successful! Installer is available in the {OUTPUT_DIR} directory.")
        else:
            print("\nBuild incomplete. Please check the errors above.")
        
    except Exception as e:
        print(f"Error during build: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
