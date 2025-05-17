# --------------------------------------------
# Import necessary modules
# --------------------------------------------
from flask import Flask                     # Core Flask framework
# SQLAlchemy extension for ORM/database handling
from flask_sqlalchemy import SQLAlchemy
# CORS (Cross-Origin Resource Sharing) support for frontend-backend communication
from flask_cors import CORS

# --------------------------------------------
# Initialize Flask application
# --------------------------------------------
app = Flask(__name__)

# Enable CORS for all routes, allowing the app to handle requests from different origins (e.g., React/Vue frontend)
CORS(app)

# --------------------------------------------
# Configure Database
# --------------------------------------------

# Set the database URI to use a local SQLite database named 'mydatabase.db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# Disable SQLAlchemy event notifications to save memory (optional but recommended)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# --------------------------------------------
# Initialize SQLAlchemy with Flask app
# --------------------------------------------
db = SQLAlchemy(app)
