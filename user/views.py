__author__ = 'Joshua'

from SeraphNav import app, db, salt
from flask import request, redirect, render_template, session, url_for
from user.models import User
from website.models import Nav
from form import RegisterForm, LoginForm
import bcrypt


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
        ).first()
        if user:
            if bcrypt.hashpw(form.password.data, salt) == user.password:
                session['username'] = user.username
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('index'))
            else:
                error = "Incorrect password"
        else:
            error = "User not found"
    return render_template('user/login.html', form=form, error=error)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            form.email.data,
            form.username.data,
            bcrypt.hashpw(form.password.data, salt)
        )
        db.session.add(user)
        db.session.commit()

        nav = Nav(
            user.id
        )
        db.session.add(nav)
        db.session.commit()

        return redirect('/login')
    return render_template('user/register.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


@app.route('/success')
def success():
    return "Registered!"