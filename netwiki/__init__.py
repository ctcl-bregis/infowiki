# NetWiki - CTCL 2024
# File: /src/__init__.py
# Purpose: 
# Created: November 11, 2024
# Modified: November 11, 2024

__version__ = "0.1.0"

# External module imports
from flask import Flask
import logging
import sys

# Local module imports
from . import config

# Logger setup
logger = logging.getLogger(__name__)

def create_app():    
    logging.basicConfig(level = logging.INFO)

    cfg = config.loadconfig()
    # Stop execution if the config did not load due to an error
    if not cfg:
        sys.exit()

    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder="config/templates",
        static_folder="config/static"
    )

    # This supposedly allows the config to be accessed globally
    app.config["APPCONFIG"] = cfg.model_dump_json()
    
    from . import routes
    app.register_blueprint(routes.bp)

    return app
