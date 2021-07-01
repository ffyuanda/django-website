from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
import data

app = Flask(__name__)

contact = data.Contact()

@app.route("/")
def blog():
    return render_template('blog.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/login', methods=['POST', 'GET'])
@app.route('/login/<name>')
def login(name=None):
    return render_template('login.html', name=name)
