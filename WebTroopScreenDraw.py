import sys
import os

# Add the src directory to the path so we can import modules from there
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.screen_draw import main

if __name__ == "__main__":
    main()
