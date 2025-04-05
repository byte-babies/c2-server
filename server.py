from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/buttoncatcher', methods=['POST'])
def buttoncatcher():
    print(request.method)
    if request.method == 'POST':
        print("I GOT SOMETHING!")
        return {"status": "success"}

if __name__ == "__main__": # if running this file directly
    app.run(debug=True) # run the app
