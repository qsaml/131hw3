from myapp import myobj
from myapp import db
from myapp.forms import LoginForm, TopCities
from myapp.models import Cities
from flask import render_template, escape, flash, redirect

@myobj.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html")

@myobj.route("/hi")
def hi():
    return "Hi!"

@myobj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        return redirect('/')

    return render_template('login.html', form=form)

@myobj.route("/members/<string:name>")
def getMember(name):
    return "hi: " + escape(name)

@myobj.route("/main")
def main():
    date = '2021-10-05'
    users = {'username':'carlos'}

    post = [ { 'author': 'John', 'body' : 'Beatutiful day in Portland!'},\
            { 'author' : 'Susan', 'body' : 'The day is cloudy today!'}]

    return render_template('hello.html', users=users, datee=date, post=post)

@myobj.route("/home", methods=['GET', 'POST'])
def home_hw():
    title = 'Top Cities'
    name = 'Sam'
    form = TopCities()

    if form.validate_on_submit():
        flash(f'{form.city_name.data} added at position {form.city_rank.data}')
        city = form.city_name.data
        rank = form.city_rank.data
        ranked_city = Cities()
        db.session.add(ranked_city)
        return redirect('/home')
    return render_template('home.html', title=title, name=name, form=form)
