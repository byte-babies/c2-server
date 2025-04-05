from flask import Flask, render_template, request
import argparse
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

PORT = 5000

@app.route('/')
def index():
    return render_template("index.html", port=PORT)

@app.route('/paramreader')
def paramreader():
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
    PORT = parser.parse_args().port
    app.run(host="0.0.0.0", port=PORT, debug=True)
