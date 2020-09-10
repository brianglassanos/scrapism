from flask import Flask 
app = Flask(__name__)

@app.route('/')
def title_one():
    return 'SCRAPISM v1.0'

@app.route('/about')
def about():
    return 'Scrapism is a BS4 web scraper for finding business website contact/support information.'