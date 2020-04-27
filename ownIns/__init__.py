# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config.from_pyfile('app.conf')
# for break or continue
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
db = SQLAlchemy(app)

from ownIns import views, models

