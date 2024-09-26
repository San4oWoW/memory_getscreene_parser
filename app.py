import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open('data.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
    return render_template("index.html", data=json.dumps(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)