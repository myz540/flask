from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

# the decorators are used to associate certain URLs with view functions
# in this case, the index() view is invoked when either URL / or /index are passed


@application.route('/')
@application.route('/index')
def index():
    dummy_user = {'username': 'Mike Zhong'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(url_for('index'), title='Home', user=dummy_user, posts=posts)


@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me= {}".format(
            form.username.data, form.remember_me.data))

        return redirect(url_for('index'))

    return render_template(url_for('login'), title='Sign In', form=form)