# WebtroopsScreen Draw

A professional screen drawing tool that allows you to draw directly on your screen with hotkeys.

## Features

- Draw directly on your screen with hotkeys
- Choose from multiple colors
- Add text to your drawings
- Clear drawings without exiting
- Global hotkey activation (F9)

## Installation

### Windows Installer

1. Download the latest installer from the [Releases](https://github.com/YourUsername/WebTroopScreenDraw/releases) page
2. Run the installer and follow the instructions
3. Launch WebtroopsScreen Draw from the Start menu or desktop shortcut
4. Press F9 to activate drawing mode

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
└── README.md           # This file
```

## License

MIT License - See LICENSE file for details.

## Credits

Developed by WebTroop
