# NetWiki - CTCL 2024
# File: /wsgi.py
# Purpose: App entry point
# Created: November 11, 2024
# Modified: November 11, 2024

import os
import sys
from netwiki import create_app
sys.path.append(os.path.dirname(__name__))

app = create_app()

if __name__ == "__main__":
    
    if sys.argv[1]:
        if sys.argv[1] == "--debug":
            debug = True
        else:
            debug = False
    else:
        debug = False
    
    
    app.run(debug = debug)