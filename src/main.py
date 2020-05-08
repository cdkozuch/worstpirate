from flask import Flask, send_file, make_response
from doplot import do_plot

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>That is, without doubt, the worst pirate I've ever seen.</h1>"

@app.route('/plot', methods=['GET'])
def correlation_matrix():
    bytes_obj = do_plot()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)