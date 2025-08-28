import os
import sys
import shutil
import subprocess

APP_NAME = "WebtroopsScreen Draw"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A screen drawing tool that lets you draw on any window"
APP_PUBLISHER = "Webtroop"
APP_URL = "https://github.com/webtroop/screen-draw"

DIST_DIR = os.path.join(os.getcwd(), "dist")
BUILD_DIR = os.path.join(os.getcwd(), "build")
ASSETS_DIR = os.path.join(os.getcwd(), "assets")
ICON_PATH = os.path.join(ASSETS_DIR, "icon.ico")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")
INSTALLER_OUTPUT = os.path.join(OUTPUT_DIR, f"{APP_NAME.replace(' ', '')}_Setup_{APP_VERSION}.exe")

# Common Inno Setup installation paths
INNO_SETUP_PATHS = [
    r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
    r"C:\Program Files\Inno Setup 6\ISCC.exe",
    r"C:\Program Files (x86)\Inno Setup 5\ISCC.exe",
    r"C:\Program Files\Inno Setup 5\ISCC.exe"
]

def find_inno_setup():
    """Find the Inno Setup compiler executable"""
    for path in INNO_SETUP_PATHS:
        if os.path.exists(path):
            return path
            
    # Ask user for the path if not found
    print("Inno Setup compiler not found in common locations.")
    user_path = input("Please enter the full path to ISCC.exe (Inno Setup Compiler): ")
    if os.path.exists(user_path):
        return user_path
    else:
        print(f"Error: The path {user_path} does not exist.")
        return None

def clean_directories():
    """Clean output and build directories"""
    print("Cleaning output directories...")
    for directory in [DIST_DIR, BUILD_DIR, OUTPUT_DIR]:
        if os.path.exists(directory):
            shutil.rmtree(directory)
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Output directories cleaned")

def build_executable():
    """Build executable with PyInstaller"""
    print("Building executable with PyInstaller...")
    cmd = [
        "pyinstaller",
        "--windowed",
        "--onefile",
        "--clean",
        f"--icon={ICON_PATH}",
        f"--name={APP_NAME}",
        "WebTroopScreenDraw.py"
    ]
    
    result = subprocess.run(cmd, capture_output=False)
    
    if result.returncode != 0:
        print("Error: PyInstaller build failed.")
        sys.exit(1)
    
    print("Executable build complete")

def create_inno_setup_script():
    """Create Inno Setup script file"""
    print("Creating Inno Setup script...")
    
    script_content = f"""
#define MyAppName "{APP_NAME}"
#define MyAppVersion "{APP_VERSION}"
#define MyAppPublisher "{APP_PUBLISHER}"
#define MyAppURL "{APP_URL}"
#define MyAppExeName "{APP_NAME}.exe"

[Setup]
AppId={{{{{APP_NAME.replace(' ', '_')}}}}}
AppName={{#MyAppName}}
AppVersion={{#MyAppVersion}}
AppPublisher={{#MyAppPublisher}}
AppPublisherURL={{#MyAppURL}}
AppSupportURL={{#MyAppURL}}
AppUpdatesURL={{#MyAppURL}}
DefaultDirName={{autopf}}\\{{#MyAppName}}
DisableProgramGroupPage=yes
LicenseFile=LICENSE
OutputDir={OUTPUT_DIR.replace('\\', '\\\\')}
OutputBaseFilename={APP_NAME.replace(' ', '')}_Setup_{APP_VERSION}
SetupIconFile={ICON_PATH.replace('\\', '\\\\')}
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"
Name: "quicklaunchicon"; Description: "{{cm:CreateQuickLaunchIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; OnlyBelowVersion: 0,6.1

[Files]
Source: "{DIST_DIR.replace('\\', '\\\\')}\\{{#MyAppExeName}}"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{ASSETS_DIR.replace('\\', '\\\\')}\\*"; DestDir: "{{app}}\\assets"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "LICENSE"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{{app}}"; Flags: ignoreversion isreadme

[Icons]
Name: "{{group}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"
Name: "{{commondesktop}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: desktopicon

[Run]
Filename: "{{app}}\\{{#MyAppExeName}}"; Description: "{{cm:LaunchProgram,{{#StringChange(MyAppName, '&', '&&')}}}}"; Flags: nowait postinstall skipifsilent
"""
    
    with open("installer_script.iss", "w") as f:
        f.write(script_content)
    
    print("Inno Setup script created")

def build_installer(iscc_path):
    """Build installer with Inno Setup"""
    print("Building installer with Inno Setup...")
    
    result = subprocess.run([iscc_path, "installer_script.iss"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: Inno Setup build failed.\n{result.stderr}")
        sys.exit(1)
    
    print(f"Installer built successfully: {INSTALLER_OUTPUT}")

def main():
    """Main build process"""
    print(f"Building {APP_NAME} v{APP_VERSION}")
    
    # Find Inno Setup compiler
    iscc_path = find_inno_setup()
    if not iscc_path:
        print("Error: Inno Setup not found. Please install Inno Setup.")
        print("Download from: https://jrsoftware.org/isdl.php")
        sys.exit(1)
    
    clean_directories()
    build_executable()
    create_inno_setup_script()
    build_installer(iscc_path)
    
    print(f"Build complete! Installer is available at: {INSTALLER_OUTPUT}")

if __name__ == "__main__":
    main()
