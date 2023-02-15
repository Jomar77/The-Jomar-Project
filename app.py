from flask import Flask, render_template, request

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)





@app.route('/', methods = ['GET', 'POST'])
def home():  
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
    return render_template('index.html')

@app.route('/2021.html', methods = ['GET', 'POST'])
def year1():
    return render_template("2021.html")

@app.route('/2022.html', methods = ['GET', 'POST'])
def year2():
    return render_template("2022.html")

@app.route('/2023.html', methods = ['GET', 'POST'])
def year3():
    return render_template("2023.html")

if __name__ == '__main__':
    app.run(debug=True)