from myapp import myobj
from myapp.forms import LoginForm, TopCities
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

@myobj.route("/home")
def home_hw():
    title = 'Top Cities'
    name = 'Sam'
    form = TopCities()

    return render_template('home.html', title=title, name=name)
