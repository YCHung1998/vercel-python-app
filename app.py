from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/about')
def about():
    return 'The about page to show that smthing your might to know'



@app.route('/api')
def api():
    return "api link is working" 


