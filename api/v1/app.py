#!/usr/bin/python
"""Flask entry point"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

# Create Flask instance
app = Flask(__name__)

# Register blueprint to app
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={"*": {"origins": "0.0.0.0"}})

# Declare method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_appcontext(error):
    storage.close()

# Declare method to handle 404 error
@app.errorhandler(404)
def resource_not_found(e):
    """ throws 404 error on bad routes """
    return jsonify({"error": "Not found"}), 404

# Run Flask server
if __name__ == "__main__":
    # Define host and port
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)

    # Run Flask server with defined host and port
    app.run(host=host, port=port, threaded=True)
