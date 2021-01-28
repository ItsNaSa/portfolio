# app.py

# Imports
import os
import firebase_admin
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from flask.helpers import make_response
import pyrebase

# Initialize the flask app
app = Flask(__name__)

cred = credentials.Certificate('./portfolioKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/", methods = ["GET"])
def home():
    return "Welcome to my portfolio!!"

@app.route("/addContact", methods=["GET", "POST"])
def addContact():
    if request.method == "GET":
        a = db.collection(u'contact').stream()
        for x in a:
            print(f'{x.id} => {x.to_dict()}')
        return make_response(({"Unsuccessful": True}), 200)