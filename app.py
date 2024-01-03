from flask import Flask, render_template, url_for, request
import sqlite3
from datetime import datetime
import hashlib

con = sqlite3.connect("paste.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS paste(idx INTEGER PRIMARY KEY, title TEXT, date DATE, data TEXT);")

con.commit()

con.close()

app = Flask(__name__)

def tuple_to_dict(d,t):
    idx,title,data = t
    if title:
        d.setdefault(title, data)
    else:
        d.setdefault(idx,data)
    return d



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/paste", methods=['POST','GET'])
def paste():
    if request.method == 'POST':
        idx = 0 
        con = sqlite3.connect('paste.db')
        cursor = con.cursor()
        value = request.form['paste']
        title = request.form["paste-title"]
        date = str(datetime.now()).split(".")[0]
        res = cursor.execute(f"SELECT idx FROM paste;")
        try:
            idx, = res.fetchall()[-1]
            idx += 1
        except:
            pass
        cursor.execute(f"INSERT INTO paste VALUES (?, ?, ?,?);",(idx, title, date, value))
        #SELECT col1,col2... FROM db ORDER BY col1
        #SELECT col1 FROM db WHERE idx='idx_2'
        con.commit()
        con.close()

    
    con = sqlite3.connect('paste.db')
    cursor = con.cursor()
    res = cursor.execute("SELECT idx, title, data FROM paste")
    values = res.fetchall()
    dic = {}
    for value in values:
        tuple_to_dict(dic,value)
    con.close()
    return render_template("paste.html", pastes=dic)
    
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

@app.route('/paste/<int:paste_idx>')
def retreive_paste(paste_idx):
    pass


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')

