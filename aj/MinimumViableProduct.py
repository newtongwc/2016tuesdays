from flask import Flask
from flask import request

# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask('Adventure', static_url_path='')

# By default, Flask serves the file index.html if there's no path after
# the URL. This overrides that default to send the static file adventure.html
# instead (found in ./static/adventure.html)
@app.route("/")
def Topic():
    return app.send_static_file('Topic.html')

@app.route("/this", methods=['POST'])
def addRegion():
    print("I got it!")
    print (request.form['drink'])


app.run()
