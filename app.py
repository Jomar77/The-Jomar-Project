from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():  
    
    return render_template('index.html')

@app.route('/blogs.html', methods = ['GET', 'POST'])
def blogs():
    return render_template("blogs.html")


if __name__ == '__main__':
    app.run(debug=True)