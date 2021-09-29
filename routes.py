from control import Control
from flask import Flask, request
from models import Person
c = Control()

app_rest = Flask(__name__)
@app_rest.route("/", methods=["GET"])
def home():
    return "Hello E-Core"

@app_rest.route("/addPerson", methods=["POST"])
def addPerson():
    print(request)
    name = request.json["name"]
    age = request.json["age"]
    c.add(name, int(age))
    return "201, Pessoa Adicionada"

@app_rest.route("/listAlpha", methods=["GET"])
def listAlpha():
    listAlpha = c.showName()
    return dict(listAlpha)
        
@app_rest.route("/listAge", methods=["GET"])
def listAge():
    listAge = c.showAge()
    return dict(listAge)

@app_rest.route("/classify", methods=["POST"])
def addUser():
    name = request.json['name']
    age = request.json['age']
    person = Person(name, int(age))
    result = c.classify(person)
    return result

if __name__ == '__main__':
    app_rest.run(debug=False)