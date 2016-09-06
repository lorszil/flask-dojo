from peewee import *
from flask import Flask
import requests


db = PostgresqlDatabase("flask_dojo")
db.connect()

class BaseModel(Model):
    test = CharField()

    class Meta:
        db = db
        
db.drop_tables([BaseModel])
db.create_tables([BaseModel])


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


if __name__== "__main__":
    app.run(debug=True)
