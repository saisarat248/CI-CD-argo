from flask import Flask
from db import get_message

app = Flask(__name__)

@app.route("/")
def home():
    # Indented 4 spaces
    return get_message()

if __name__ == "__main__":
    # Indented 4 spaces
    app.run(host="0.0.0.0", port=5000)