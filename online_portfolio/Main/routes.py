from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('mobile.html', _external=True)

@main.route('/about_me')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/mobile')
def mobile():
    return render_template('index.html')