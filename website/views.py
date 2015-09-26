__author__ = 'Joshua'

from flask import render_template, redirect, request, url_for, session
from SeraphNav import app, db
from website.models import Site, Category
from user.models import User
from user.decorators import login_required
import json


@app.route('/')
@app.route('/index')
def index():
    if session.get('username'):
        username = session.get('username')
        user = User.query.filter_by(
            username=username
        ).first()
        if user:
            sites = Site.query.filter_by(
                nav_id=user.nav.first().id
            ).all()
            is_authed = True
            categories = Category.query.all()
            return render_template('site/index.html', sites=sites, categories=categories, is_authed=is_authed)
    return render_template('site/index.html')


@app.route('/share_a_site', methods=['GET', 'POST'])
@login_required
def share_a_site():
    if request.method == 'GET':
        return render_template('site/share_a_site.html', is_authed=True)
    elif request.method == 'POST':
        title = request.form['site_title']
        desc = request.form['site_desc']
        if desc == '':
            desc = title
        url = request.form['site_url']
        category_name = request.form['site_category']

        user = User.query.filter_by(
            username=session['username']
        ).first()

        category = Category.query.filter_by(
            name=category_name
        ).first()

        if category is None:
            category = Category(category_name)

        site = Site(user.nav.first(), title, desc, url, category)
        db.session.add(site)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    result = []
    for category in categories:
        result.append({'name':category.name})
    return json.dumps(result)