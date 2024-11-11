# NetWiki - CTCL 2024
# File: /routes.py
# Purpose: 
# Created: November 11, 2024
# Modified: November 11, 2024

from flask import Blueprint
from netwiki import views

bp = Blueprint("routes", __name__)

bp.add_url_rule("/debug/", view_func = views.debug)


