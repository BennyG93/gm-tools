from flask import render_template, flash, redirect, url_for
from webapp import app
from webapp.forms import QuickScoutForm, GMLoginForm
from webapp.controllers.gmtools.gmtools.login import gm_login
from webapp.controllers.gmtools.gmtools.hire import gm_hire

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = GMLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        gm_login(username, password)
        return redirect(url_for('quickscout'))
    return render_template('index.html', form=form)

@app.route('/quickscout', methods=['GET', 'POST'])
def quickscout():
    form = QuickScoutForm()
    if form.validate_on_submit():
        total_turns = form.total_turns.data
        turns_interval = form.turns_interval.data
        scout_choice = form.scout_choices.data
        headless = form.headless.data
        print(headless)
        gm_hire(total_turns, turns_interval, scout_choice, headless)
        return redirect(url_for('quickscout'))
    return render_template('quickscout.html', form=form)
