import PyInstaller.__main__
import os
import shutil

# Create a build directory if it doesn't exist
if not os.path.exists('build'):
    os.makedirs('build')

# Clean any previous build artifacts
if os.path.exists('dist'):
    shutil.rmtree('dist')

# Run PyInstaller
PyInstaller.__main__.run([
    'WebTroopScreenDraw.py',
    '--name=ScreenDraw',
    '--onefile',
    '--windowed',
    '--add-data=src;src',
    '--icon=resources/icon.ico',  # Replace with your icon if you have one
])

print("Build completed successfully!")
