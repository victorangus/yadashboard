# -*- coding: utf-8 -*-
from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask
from flask import render_template
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('yadashboard.html')

'''
@app.route('/template/')
@app.route('/template/<name>')
def template(name=None):
    return render_template('template.html', name=name)
'''

@app.route('/geo')
def geo():
    return render_template('geo.html')

@app.route('/env')
def env():
    return render_template('env.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    try:
        from google.appengine.ext.webapp.util import run_wsgi_app
    except ImportError:
        app.run(debug=True)
    else:
        run_wsgi_app(app)
