import sys
import os

# Fix for module path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.login_ui import open_login

# Start App
if __name__ == "__main__":
    open_login()