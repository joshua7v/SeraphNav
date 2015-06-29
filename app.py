__author__ = 'Joshua'

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {"db": "SeraphNav"}
db = MongoEngine(app)
app.config.from_object(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/index')
def index():
    from model import Site
    sites = Site.objects.all()
    return render_template('index.html', sites=sites)


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/share_a_site', methods=['GET', 'POST'])
def share_a_site():
    if request.method == 'GET':
        return render_template('share_a_site.html')
    elif request.method == 'POST':
        title = request.form['site_title']
        desc = request.form['site_desc']
        url = request.form['site_url']
        from model import Site
        site = Site(title, desc, url)
        site.save()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = False
    app.run()