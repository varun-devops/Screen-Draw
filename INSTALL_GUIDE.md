# Installation Guide for WebtroopsScreen Draw

This guide provides step-by-step instructions for installing WebtroopsScreen Draw on any Windows computer.

## Method 1: Using the Installer (Recommended)

1. **Download the Installer**
   - Go to: [https://github.com/varun-devops/Screen-Draw/releases](https://github.com/varun-devops/Screen-Draw/releases)
   - Download the latest `WebtroopsScreen Draw_Setup_x.x.x.exe` file

2. **Run the Installer**
   - Right-click the downloaded file and select "Run as administrator" (recommended)
   - If a security warning appears, click "More info" and then "Run anyway"

3. **Follow the Installation Wizard**
   - Choose your installation options:
     - Installation location (default recommended)
     - Desktop shortcut (recommended)
     - Start menu shortcuts (recommended)
     - Start automatically with Windows (optional)
     - Register global hotkey (F9) (recommended)

4. **Complete Installation**
   - Click "Install" to begin installation
   - Wait for the installation to complete
   - Check "Launch WebtroopsScreen Draw" if you want to start immediately
   - Click "Finish"

5. **Using the Application**
   - Press `F9` anywhere to start drawing on your screen
   - Use the color buttons at the bottom to change drawing color
   - Click the "TEXT" button to add text annotations
   - Click the "RESET" button to clear all drawings
   - Press `ESC` to exit drawing mode

## Method 2: Manual Installation

If you prefer to run the application without installation:

1. **Download the Source Code**
   - Go to: [https://github.com/varun-devops/Screen-Draw](https://github.com/varun-devops/Screen-Draw)
   - Click the green "Code" button and select "Download ZIP"
   - Extract the ZIP file to a location of your choice

2. **Install Prerequisites**
   - Install Python 3.8 or newer from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation
   - Open Command Prompt as administrator
   - Navigate to the extracted folder:
     ```
     cd path\to\extracted\folder
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Application**
   - In the same Command Prompt window:
     ```
     python WebTroopScreenDraw.py
     ```
   - Or double-click the `WebTroopScreenDraw.py` file if Python is set as the default application

4. **Create a Shortcut (Optional)**
   - Right-click on `WebTroopScreenDraw.py` and select "Create shortcut"
   - Move the shortcut to your desktop or Start menu
   - To start with Windows, run the included script:
     ```
     python setup_shortcut.bat
     ```

## Troubleshooting

- **If the global hotkey (F9) doesn't work**: Try running the application as administrator
- **If the application doesn't start**: Check that you have the required dependencies installed
- **For other issues**: Visit our [GitHub issues page](https://github.com/varun-devops/Screen-Draw/issues)

## Uninstalling

- Go to Control Panel > Programs > Programs and Features
- Select "WebtroopsScreen Draw" and click "Uninstall"
- Follow the uninstallation wizard

## Support

For help or to report issues:
- Open an issue on [GitHub](https://github.com/varun-devops/Screen-Draw/issues)
- Contact us at your-email@example.com
