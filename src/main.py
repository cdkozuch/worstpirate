from flask import Flask, send_file, make_response, render_template
from argparse import ArgumentParser

from fractal import generate_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['GET'])
def get_plot():
    bytes_obj = generate_plot()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

if __name__ == "__main__":
    parser = ArgumentParser("Simple Web App")
    parser.add_argument('-e', '--flask_env', required=True, type=str,
        choices=['prod', 'dev'], help="choose production or development environment")

    args = parser.parse_args()

    if args.flask_env == 'prod':
        from waitress import serve
        serve(app, host="0.0.0.0", port=80)
    else:
        app.debug = True
        app.run(host="0.0.0.0", port=8080)