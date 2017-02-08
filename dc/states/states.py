from flask import Flask
from flask import render_template
from flask import request

app = Flask('States', static_url_path='')

@app.route("/")
def show_states_home():
   return app.send_static_file('states_home.html')

app.run()
