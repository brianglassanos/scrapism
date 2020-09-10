from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

# main routing
@app.route('/')
def title_one():
    return 'SCRAPISM v1.0'

@app.route('/about')
def about():
    return 'Scrapism is a BS4 web scraper for finding business website contact/support information.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/github')
def get_github():
    return 'Follow me on GitHub: @brianglassanos (https://github.com/brianglassanos)'

# subpath routing
@app.route('/user/<username>')
def profile(username):
    # show user profile for current user
    return '{}\'s profile'.format(escape(username))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show post integer id
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show subpath after /path/
    return 'Subpath %s' % escape(subpath)

# path reversal -- for easy changing of functions
with app.test_request_context():
    print(url_for('about'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('get_github'))
    
    # CSS file
    print(url_for('static', filename='style.css'))
    
    print(url_for('show_post', post_id='1'))
    print(url_for('profile', username='John Doe'))
