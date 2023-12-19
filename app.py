from flask import Flask, render_template, url_for
import sqlite3
#import request

con = sqlite3.connect('paste.db')

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS paste (data TEXT,date DATE,id INTEGER)")

con.commit()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("paste.html")

@app.route("/paste", methods=['POST','GET'])
def posting():
    if request.method == 'POST':
        print('executed')
    if request.method == 'GET':
        return render_template("paste.html")



if __name__=="__main__":
    app.run(debug=True)

