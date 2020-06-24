# -*- coding: utf-8 -*-



from __future__ import with_statement
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask, request, session, url_for, redirect, \
    render_template, abort, g, flash
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)


a = None
b = None
c = None
cal = None

text1 = None
text2 = None

text3 = None
text=None

@app.route('/')

def jinja2():
   return render_template('exp4.html')

@app.route('/note')
@app.route('/<n>/note')
def note(n=None):
    if n== 1 :
        subject = "머신러닝"
    elif n==2 :
        subject = "정보시스템 통합 및 실습"
    else:
        subject = "산업 AI"
        return render_template('note.html',n=n, subject=subject, text=text)


@app.route('/save',methods=['POST'])
def save():
    global text

    if request.method == 'POST':
        text = request.form['text']
        return redirect(url_for('note'))



@app.route('/sessions')
def sessions():
    """calculator"""
    global a
    global b
    global c
    global cal

    if a is not None and b is not None:
        if cal=='+':
            c = str(float(a) + float(b))
        elif cal == '-':
            c = str(float(a) - float(b))
        elif cal =='*':
            c = str(float(a) * float(b))

        elif cal == '/':
            c = str(float(a) / float(b))
        else:
            cal = None
    return render_template('cal.html', num=a ,num2=b, num3=c, cal=cal)

@app.route('/calculate2',methods=['POST'])
def calculate2():
    global a
    global b
    global cal

    if 'plus' in request.form:
        cal = '+'
    elif 'minus' in request.form:
        cal = '-'
    elif 'mul' in request.form:
        cal = '*'
    elif 'div' in request.form:
        cal = '/'
    else:
        cal = None

    if request.method == 'POST':
        if request.form['num']!='' and request.form['num2']!='':
            a = request.form['num']
            b = request.form['num2']
            return redirect(url_for('sessions'))
        else:
            a = request.form['num']
            b = request.form['num2']
            if a =='':
                if b =='':
                    a = None
                    b = None
                else:
                    a = None
            else:
                b = None
            return redirect(url_for('sessions'))



if __name__ == '__main__':
  app.run()
