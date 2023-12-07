from flask import Flask, render_template, url_for
import sqlite3

con = sqlite3.connect('paste.db')

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS paste (data TEXT,date DATE,id INTEGER)")

con.commit()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("paste.html", name = 'skillz')

if __name__=="__main__":
    app.run(debug=True)

