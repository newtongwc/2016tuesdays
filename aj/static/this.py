from flask import Flask
from flask import request

@app.route("this", methods=['POST'])
def addRegion():
    print("I got it!")
    print (request.form['drink'])
