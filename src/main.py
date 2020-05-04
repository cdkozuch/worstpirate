from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>That is, without doubt, the worst pirate I've ever seen.</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)