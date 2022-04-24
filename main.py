from flask import Flask
from flask import render_template
from flask import request
from  write import writerXlsx
import rapidminer
import pandas as pd
app = Flask(__name__,static_url_path='/static')

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
    rm = rapidminer.Studio()
    myinput = pd.read_excel(r'test.xlsx')
    run_model = rm.run_process("//Local Repository/DataMining/Deployment", inputs=[myinput])
    myoutput = rm.read_resource("//Local Repository/data/Output")
    resultStr = myoutput["prediction(Faculty)"].to_string()
    result = resultStr.split("    ")
    return  render_template('result.html', result= result[1])# 
    
app.run(debug=True)
