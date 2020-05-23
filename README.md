# GM Tools
A Python based project use to automate common gameplay actions in a web game I play. Flask is used as a web front end which calls selenium automation functions running in the Chromedriver.

Setup:
```
python3 -m venv venv
source venv/bin/activate
```

Run locally:
```
export FLASK_APP=gm-tools.py
flask run
```

Build and distribute packaged binary:
(final package in `dist/`)
```
pyinstaller --onefile --icon=icon.ico --add-data 'webapp:webapp' gm-tools.py
```
