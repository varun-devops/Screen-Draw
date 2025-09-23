# Creating a GitHub Release for WebtroopsScreen Draw v1.0.1

Follow these steps to create a GitHub release and upload your installer for the 1.0.1 update.

## Steps to Create a GitHub Release

1. Go to your repository on GitHub: [https://github.com/varun-devops/Screen-Draw](https://github.com/varun-devops/Screen-Draw)

2. Click on the "Releases" section on the right-hand side of your repository

3. Click on "Create a new release" or "Draft a new release"

4. Fill in the following details:
   - Tag version: `v1.0.1`
   - Release title: `WebtroopsScreen Draw v1.0.1`
   - Description: Copy and paste the description below

5. Upload the installer:
   - Drag and drop or click to upload the `WebtroopsScreen Draw_Setup_1.0.1.exe` file from your `Output` folder

6. Click "Publish release"

## Release Description Template

```
# WebtroopsScreen Draw v1.0.1

This update fixes the configuration file error that users experienced when running the application after installation.

## What's Fixed

- Fixed the configuration file error that occurred when users downloaded and ran the application
- Configuration files are now stored in user's home directory (`~/ScreenDraw/`) instead of temporary locations
- Improved error handling for configuration file loading and saving
- Added better error messages for configuration-related issues

## Installation

1. Download the `WebtroopsScreen Draw_Setup_1.0.1.exe` installer
2. Run the installer
3. Follow the on-screen instructions
4. Launch from the Start menu or desktop shortcut
5. Press the configured hotkey (default: Ctrl+Shift+D) to start drawing on your screen

## System Requirements

- Windows 10/11
- 4GB RAM minimum
```

## Important Notes

1. Push all changes to GitHub before creating the release:
   ```
   git add .
   git commit -m "Fix config file location issue in v1.0.1"
   git push origin main
   ```

2. After publishing the release, monitor GitHub issues for any feedback or reports from users.