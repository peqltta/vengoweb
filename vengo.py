from flask import Flask, render_template

app = Flask(__name__,static_url_path="", static_folder="static")

@app.route("/")
def hello_world():
    return render_template('index.html')

app.run(host='0.0.0.0', port='5000', debug=True)
