from flask import Flask, jsonify, request
import platform, json
from random import choice

app = Flask(__name__)

@app.route("/", methods=["GET"])
def Joke():
    # Use different path if host is windows/linux
    def path():
        if platform.system() == "Windows":
            return "data\\"
        else:
            return "./data/"
    # Get Authorization value from request Header
    api_key = request.headers.get('Authorization')
    # Get API keys from json/database
    with open(f"{path()}api_keys.json") as f:
        keys = json.load(f)
    # Check if API is in the database
    if api_key in keys["keys"]:
        # Open json/database with jokes and get a random joke
        with open(f"{path()}jokes.json") as f:
            jokes = json.load(f)
        random_joke = choice(jokes["jokes"])
        return jsonify({"joke":random_joke})
    else:
        return jsonify({"error":"Unknown API Key"})

if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=80)