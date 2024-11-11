# NetWiki - CTCL 2024
# File: /views.py
# Purpose: 
# Created: November 11, 2024
# Modified: November 11, 2024

from flask import current_app

def debug():
    config = current_app.config

    raise Exception