from flask import Flask
from flask import render_template
import duolingo
import json

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("index.html")


lingo = duolingo.Duolingo('MojNac','7M36veGfShEWkQh')
json_file = json.dumps(lingo.get_streak_info(), indent=4)
with open("duo.json", "w") as outfile:
    outfile.write(json_file)