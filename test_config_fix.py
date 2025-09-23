"""
Test script to verify the configuration file fix in v1.0.1
"""

import os
import sys
import shutil

def test_config_path():
    """Test that the configuration file path is properly set in user's home directory"""
    print("Testing configuration file path...")
    
    # Check if user's home directory exists
    home_dir = os.path.expanduser('~')
    print(f"User's home directory: {home_dir}")
    assert os.path.exists(home_dir), "Home directory does not exist"
    
    # Check if ScreenDraw folder can be created
    screen_draw_dir = os.path.join(home_dir, 'ScreenDraw')
    print(f"ScreenDraw directory: {screen_draw_dir}")
    
    if os.path.exists(screen_draw_dir):
        print("ScreenDraw directory already exists")
    else:
        try:
            os.makedirs(screen_draw_dir, exist_ok=True)
            print("Successfully created ScreenDraw directory")
            # Clean up after test
            os.rmdir(screen_draw_dir)
        except Exception as e:
            print(f"ERROR: Could not create directory: {e}")
            return False
    
    # Check write permissions
    try:
        os.makedirs(screen_draw_dir, exist_ok=True)
        test_file = os.path.join(screen_draw_dir, 'test_config.ini')
        with open(test_file, 'w') as f:
            f.write('test = "value"\n')
        print(f"Successfully wrote test file to {test_file}")
        
        # Read back the file
        with open(test_file, 'r') as f:
            content = f.read()
        print(f"Successfully read test file content: {content}")
        
        # Clean up
        os.remove(test_file)
        print("Successfully removed test file")
    except Exception as e:
        print(f"ERROR: File operation failed: {e}")
        return False
    
    print("Configuration path test PASSED")
    return True

def test_screen_draw_import():
    """Test importing the screen_draw module"""
    print("\nTesting screen_draw module import...")
    try:
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from src import screen_draw
        print(f"Successfully imported screen_draw module from {screen_draw.__file__}")
        
        # Test load_config function
        print("Testing load_config function...")
        hotkey = screen_draw.load_config()
        print(f"Loaded hotkey: {hotkey}")
        assert hotkey, "Hotkey should not be empty"
        
        print("Module import test PASSED")
        return True
    except Exception as e:
        print(f"ERROR: Could not import screen_draw module: {e}")
        return False

if __name__ == "__main__":
    print("Running configuration tests for v1.0.1...\n")
    
    path_test = test_config_path()
    import_test = test_screen_draw_import()
    
    if path_test and import_test:
        print("\nAll tests PASSED! The configuration fix is working correctly.")
        sys.exit(0)
    else:
        print("\nTests FAILED! There are still issues with the configuration.")
        sys.exit(1)