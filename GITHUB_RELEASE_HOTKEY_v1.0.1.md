# Updated Hotkey Information for WebtroopsScreen Draw v1.0.1

The configuration system for WebtroopsScreen Draw has been updated in v1.0.1. This document explains the changes to how hotkeys are handled.

## Configuration File Location

In v1.0.1, the configuration file is now stored in the user's home directory:

```
~/ScreenDraw/config.ini
```

This location is accessible and writable by the application regardless of whether it's running in development mode or as a packaged executable.

## Default Hotkey

The default hotkey has been set to `ctrl+shift+d`, which is more intuitive and less likely to conflict with other applications.

## Customizing the Hotkey

Users can customize the hotkey by editing the `config.ini` file in their home directory. The format is:

```
hotkey = "your_hotkey_here"
```

Supported hotkeys include:
- `F1` to `F12` function keys
- Modifier combinations like `ctrl+shift+d`
- Alt key combinations like `alt+z`

## Technical Implementation

The `load_config()` function in `src/screen_draw.py` now:

1. Checks if running as frozen executable or in development
2. Creates a config directory in user's home folder if it doesn't exist
3. Reads/writes the configuration file from that location
4. Falls back to default hotkey if there are any issues

This ensures a consistent experience for all users, regardless of how they installed the application.