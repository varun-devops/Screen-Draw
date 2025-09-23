# Screen Draw Application

A tool for drawing on your screen during presentations or for annotations.

## Installation

1. Download the latest release from the GitHub releases page
2. Extract the ZIP file
3. Run `ScreenDraw.exe`

## Usage

- Press `Ctrl+Shift+D` (default) to activate drawing mode
- Draw on your screen using your mouse
- Press `Esc` to exit drawing mode

## Configuration

The application creates a configuration file in the `config` directory. You can modify the hotkey by editing `config/config.py`.

## Troubleshooting

If you encounter issues with configuration files, try running the application as administrator or ensure you have write permissions to the application directory.

## Features

- Draw directly on your screen with hotkeys
- Choose from multiple colors
- Add text to your drawings
- Clear drawings without exiting
- Global hotkey activation (F9)
- Option to start with Windows
- Minimal resource usage

## Installation

### Windows Installer (Recommended)

1. Download the latest installer from the [Releases](https://github.com/varun-devops/Screen-Draw/releases) page
2. Run the `WebtroopsScreen Draw_Setup_1.0.0.exe` installer
3. During installation, you can choose:
   - Create desktop shortcut
   - Create Start Menu shortcuts
   - Start automatically with Windows
   - Select your preferred hotkey (F9, Ctrl+Alt+W, etc.)
4. Launch WebtroopsScreen Draw from the Start menu or desktop shortcut
5. Press your chosen hotkey to activate drawing mode

### From Source

If you prefer to run from source:

1. Clone this repository
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python WebTroopScreenDraw.py
```

## Usage

- **F9 or Alt+D**: Toggle drawing mode on/off
- **Click and drag**: Draw on the screen
- **Color buttons**: Select drawing color
- **TEXT button**: Add text to your drawing
- **RESET button**: Clear all drawings
- **ESC key**: Exit drawing mode

## Building the Installer

To build the Windows installer yourself:

1. Install requirements:
```
pip install -r requirements.txt
```

2. Run the build script:
```
python build_installer.py
```

## System Requirements

- Windows 10/11
- 4GB RAM (minimum)
- 100MB disk space
- Python 3.8+ (if running from source)

## Directory Structure

```
WebTroopScreenDraw/
│
├── assets/             # Icons and other assets
│   └── icon.ico        # Application icon
│
├── src/                # Source code
│   └── screen_draw.py  # Main application code
│
├── build_installer.py  # Script to build the installer
├── requirements.txt    # Python dependencies
├── setup.py            # Package configuration
├── WebTroopScreenDraw.py  # Main entry point
├── Output/             # Contains the built installer
└── README.md           # This file
```

## License

MIT License - See LICENSE file for details.

## Credits

Developed by Webtroops
