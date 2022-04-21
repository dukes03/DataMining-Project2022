from flask import Flask
from flask import render_template
from flask import request
from  write import writerXlsx
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

@app.route('/', methods=['POST'])

def save():
    listAns = [request.form["FavoriteField"],request.form["FavoriteCamp"],request.form["MostImportantThingOfDesigning"],
    request.form["JavaJava"] ,request.form["Python"],request.form["SQL"],request.form["js"],request.form["C"]]
    #x = dict(request.form.items())
    print(listAns)
    writerXlsx(listAns)
    return "Thank you, your information is saved!"
    
app.run(debug=True)