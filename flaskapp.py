import os
import json
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


def writing(file,d):
		json.dump(d, open(file,'w'))

def reading(file):
    return  json.load(open(file))
@app.route('/sport',methods=['GET'])
def allCinemas():
    listFile=os.listdir("static/sport3/")

    result=[]
    for l in listFile:
        result.append({"id":l})
    #print result
    return jsonify(sport=result)

@app.route('/sport/<articleid>',methods=['POST'])
def tester(articleid):
    if articleid in ["0003","0004","0005","0006","0007","0008","0009","0010"]:
        writing("static/sport3/"+articleid,request.get_json())
        return "",201
    else:
        return "id must be between 0003 and 0010",422

@app.route('/sport/<articleid>',methods=['GET'])
def getCinema(articleid):
    try:
        app=reading("static/sport3/"+str(articleid))
    except Exception,e:
		return "NOT FOUND 404",404
    return jsonify(app),200




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/old/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run()
