#coding:utf8
from flask import Flask

app = Flask(__name__)
app.debug = True

from .home import home as home_print
from .admin import admin as admin_print

app.register_blueprint(home_print)
app.register_blueprint(admin_print, url_prefix="/admin")