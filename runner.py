from flask import Flask, redirect, url_for, render_template, request
import mysql.connector


def sql_connector():
    mydb =  mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Pisay_2021",)

    my_cursor = mydb.cursor()
    return mydb, my_cursor

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def home():
    if request.method == 'POST':
        mydb, my_cursor = sql_connector()
        my_cursor.execute("CREATE TABLE IF NOT EXISTS mydatabase.mytable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), message VARCHAR(255))")
        my_cursor.execute("INSERT INTO mydatabase.mytable (name, email, message) VALUES (%s, %s, %s)", (request.form['name'], request.form['email'], request.form['message']))
        mydb.commit()
        my_cursor.close()
        mydb.close()

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')