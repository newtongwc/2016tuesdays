from flask import Flask
from flask import render_template
from flask import request


# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask('Reverser', static_url_path='')

# By default, Flask serves the file index.html if there's no path after
# the URL. This overrides that default to send the static file reverse_home.html
# instead (found in ./static/reverse_home.html)
@app.route("/")
def reverse():
    return app.send_static_file('reverse_home.html')

@app.route("/reversed")
def result():
    forward = request.args.get('forward', '')
    # reversed() is a built-in python function that gives us a backward version of forward, as a list.
    # So if forward = "hello" then reversed(forward) = ["o", "l", "l", "e", "h"].
    # ''.join() joins a list together into a string by putting '' - that is, nothing - between each pair of list
    # entries next to each other.  You can also join with something besides '', like ', ' or ' and '.
    backward = ''.join(reversed(forward))
    return render_template('reverse_result.html', forward=forward, backward=backward)

app.run()
