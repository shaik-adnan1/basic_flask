from flask import Flask, render_template, jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config[
    "MONGO_URI"
] = "mongodb+srv://yousufshaik13579:Yousuf_shaik_1@test-flaskproject.mzojihz.mongodb.net/flaskTest"
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/testroute')
def test():
    return '<p>Test text</p>'

@app.route("/getdata", methods=["GET"]) 
def getData():
    data = mongo.db.data.find() # mongoDb function 

    data_list = []

    for item in data:
        item["_id"] = str(item["_id"]) # <=>
        data_list.append(item)
    print(data_list)
    return jsonify(data_list)

    # data = mongo.db.data.find()
    # data_list = [item for item in data]
    # return json.dumps(data_list)


app.run(debug=True)

## -> /getroute 
# => fetching data from the database 
# -> return
