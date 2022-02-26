from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/second")
def secondpage():
    return render_template('second.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/refer")
def refer():
    return render_template('refer.html')    

app.run(debug = True) 