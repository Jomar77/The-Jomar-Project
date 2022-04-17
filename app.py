from flask import Flask, render_template, request
import mysql.connector

def sql_connector():
    mydb =  mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Pisay_2021",)

    my_cursor = mydb.cursor()
    return mydb, my_cursor

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Pisay_2021@localhost/mydatabase'
@app.route('/', methods = ['GET', 'POST'])

def home():
    
    mydb, my_cursor = sql_connector()
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