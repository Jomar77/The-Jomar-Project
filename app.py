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

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://futnczcpmldwrl:799d6cd3f2f48f2baec2cfd9d33919688d9620ab30c227693f84b7520a9c6277@ec2-52-21-136-176.compute-1.amazonaws.com:5432/d947ktfnflnnhm'
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
    app.run(host='0.0.0.0', port=5000, debug=True)