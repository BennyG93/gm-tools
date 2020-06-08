from flask import render_template, flash, redirect, url_for
from webapp import app
from webapp.forms import QuickScoutForm
from webapp.controllers.QuickScout.quickscout.quickscout import main as gm_quickscout

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/quickscout', methods=['GET', 'POST'])
def quickscout():
    form = QuickScoutForm()
    if form.validate_on_submit():
        flash('Sit back and let the magic happen')
        username = form.username.data
        password = form.password.data
        total_turns = form.total_turns.data
        turns_interval = form.turns_interval.data
        scout_choices = form.scout_choices.data
        headless = form.headless.data
        print(headless)
        gm_quickscout(username, password, total_turns, turns_interval, scout_choices, headless)
        return redirect(url_for('quickscout'))
    return render_template('quickscout.html', form=form)
