from flask import Flask, render_template, url_for, request
import sqlite3
from datetime import datetime
import hashlib

con = sqlite3.connect('paste.db')

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS paste(data TEXT,date DATE,id INTEGER);")

con.commit()

con.close()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/paste", methods=['POST','GET'])
def paste():
    if request.method == 'POST':
        con = sqlite3.connect('paste.db')
        cursor = con.cursor()
        value = request.form['paste']
        print(value)
        date = str(datetime.now())
        res = cursor.execute(f"SELECT id FROM paste;")
        ids = res.fetchall()
        print(ids)
        cursor.execute(f"INSERT INTO paste VALUES (?);",value)
        #SELECT col1,col2... FROM db ORDER BY col1
        #SELECT col1 FROM db WHERE id='id_2'
        cursor.commit()
        con.close()

    if request.method == 'GET':
        res = cursor.execute("SELECT data FROM paste")
        test = res.fetchall()
        return render_template("paste.html")

'''
flask routing takes the following format
/route/<var_type:var_name>
var types can be:
    - string
    - int
    - float
    - path
    - uuid
'''

@app.route('/paste/<int:paste_id>')
def retreive_paste(paste_id):
    pass


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')

