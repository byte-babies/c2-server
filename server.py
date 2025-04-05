from flask import Flask, render_template, request
import argparse
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/param_reader')
def param_reader():
    print(request.args)
    flag = request.args.get('flag')
    print(f"flag is {flag}")
    return "hello warbler"

@app.route('/buttoncatcher', methods=['POST'])
def buttoncatcher():
    print(request.method)
    if request.method == 'POST':
        print("I GOT SOMETHING!")
        return {"status": "success"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port, debug=True)
