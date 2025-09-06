# wsgi.py
from app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

config_path = os.getenv("FLASK_CONFIG", "config.DevelopmentConfig")
app = create_app(config_path)
