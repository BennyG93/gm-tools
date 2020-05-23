import sys
import os
from flask import Flask
from flask_bootstrap import Bootstrap

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'webapp/templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)

# app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'not-so-secret-key'

from webapp import routes
