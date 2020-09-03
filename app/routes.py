from flask import render_template, request, redirect, json
from app import app
from app import dbHandler
from app import jsonHandler
from app.forms import usernameForm, addUserForm
import datetime


# Interface routes

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = usernameForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        return redirect('/results/' + username)
    return render_template('index.html', title='Runescape XP Tracker', form=form)


@app.route('/results/<username>/', methods=['GET', 'POST'])
def results_page(username):
    form = addUserForm()
    if form.validate_on_submit():
        if form.view.data:
            username = request.form.get('username')
            return redirect('/results/' + username)
        elif form.compare.data:
            user1 = username
            user2 = request.form.get('username')
            return redirect('/compare/'+user1+'/'+user2+'/')

    dbHandler.initialise_user_table()
    dbHandler.add_xp_record(username)
    xpRecords = dbHandler.get_xp_records_for_user(username)
    xpData = jsonHandler.create_datasets(xpRecords)
    print(xpData)
    legend = 'dates'
    labels = json.dumps(xpData[0])
    return render_template('results.html', title='Runescape XP Tracker', records=xpRecords,
                           xpcolours=jsonHandler.keyColours, xpdata=xpData, keys=jsonHandler.dictKeys, legend=legend,
                           labels=labels, username=username, form=form)


@app.route('/compare/<user1>/<user2>/', methods=['GET', 'POST'])
def compare_page(user1, user2):
    form = addUserForm()
    if form.validate_on_submit():
        if form.view.data:
            username = request.form.get('username')
            return redirect('/results/' + username)
        elif form.compare.data:
            user1 = user1
            user2 = request.form.get('username')
            return redirect('/compare/'+user1+'/'+user2+'/')

    dbHandler.initialise_user_table()
    dbHandler.add_xp_record(user1)
    xpRecords = dbHandler.get_xp_records_for_user(user1)
    xpData = jsonHandler.create_datasets(xpRecords)
    print(xpData)
    legend = 'dates'
    labels = json.dumps(xpData[0])
    return render_template('compare.html', title='Runescape XP Tracker', records=xpRecords,
                           xpcolours=jsonHandler.keyColours, xpdata=xpData, keys=jsonHandler.dictKeys, legend=legend,
                           labels=labels, username=user1, form=form)


# Data export routes

@app.route('/export/<username>.json')
def export_json(username):
    dbHandler.initialise_user_table()
    xpRecords = dbHandler.get_xp_records_for_user(username)
    return jsonHandler.create_json_export(xpRecords)


# API routes

@app.route('/api/docs')
def api_docs():
    return render_template('apidocs.html', title='Runescape XP Tracker')


@app.route('/api/user=<username>')
def api_user(username):
    return "placeholder: " + username


@app.route('/api/user=<username>&skill=<skill>')
def api_user_skill(username, skill):
    return "placeholder: " + username + " " + skill
