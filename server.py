from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
  return '<h1 style="color: red"> WELCOME TO MY APPLICATION (v2)</h1>'

app.run(host="0.0.0.0", port=4000)
