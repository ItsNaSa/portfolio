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

@app.route("/listContact", methods = ["GET"])
def listContact():
    a = db.collection(u'contact').stream()
    for x in a:
        print(f'{x.id} => {x.to_dict()}')
    return make_response(({"Unsuccessful": True}), 200)

@app.route("/addContact", methods=["POST"])
def addContact():
    contact_data = request.form.to_dict()
    db.collection(u'contact').add(contact_data)
    return make_response(({"success": True}), 201)
