from dataclasses import dataclass
from flask import Flask, render_template, request
import mysql.connector

class connect:
    def __init__(self):
        self.mydb, self.my_cursor = self.sql_connector()

    def sql_connector(i,j):
        mydb =  mysql.connector.connect(
            host = "localhost",
            user = i,
            passwd = j,
            database = "mydatabase"
            )

        my_cursor = mydb.cursor()
        return mydb, my_cursor
    
    def setInfo():
        i = str(input("Enter your database name: "))
        j = str(input("Enter your database password: "))
        return i, j

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():  
    o,p = connect.setInfo()
    mydb, my_cursor = connect.sql_connector(o,p)
    if request.method == 'POST':
        my_cursor.execute("CREATE TABLE IF NOT EXISTS mydatabase.mytable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), message VARCHAR(255))")
        my_cursor.execute("INSERT INTO mydatabase.mytable (name, email, message) VALUES (%s, %s, %s)", (request.form['name'], request.form['email'], request.form['message']))
        mydb.commit()
    
    my_cursor.execute("SELECT * FROM mydatabase.mytable")
    data = my_cursor.fetchall()
    return render_template('index.html', data = data)

@app.route('/blogs.html', methods = ['GET', 'POST'])
def blogs():
    return render_template("blogs.html")


if __name__ == '__main__':
    app.run(debug=True)