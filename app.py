from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():  
    return render_template('index.html')

@app.route('/2022.html', methods = ['GET', 'POST'])
def year1():
    return render_template("2022.html")

@app.route('/2023.html', methods = ['GET', 'POST'])
def year2():
    return render_template("2023.html")

if __name__ == '__main__':
    app.run(debug=True)