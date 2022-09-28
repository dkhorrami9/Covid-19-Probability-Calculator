'''
Title: Covid 19 Probability Calculator
Author: Dominic Khorrami-Arani
Date-created: 2022-09-27
'''

from flask import Flask, render_template, request, redirect
from pathlib import Path
import sqlite3

# --- GLOBAL VARIABLES --- #
DB_NAME = "database.db"
FIRST_RUN = True
if (Path.cwd() / DB_NAME).exists():
    FIRST_RUN = False

# --- FLASK --- #

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ALERT = ""
    if request.form:
        pass