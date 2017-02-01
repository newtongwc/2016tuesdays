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
    return app.send_static_file('mini_project_quiz.html')

# When the user goes to the website with /reversed after the base URL, show the
# reverse_result.html template, customized based on what they entered in the form.
# Note "/reversed" matches the form action in reverse_home.html.
@app.route("/grade")
def result():
    # Get the URL parameter named forward, and store it in a variable named forward.
    # If the URL doesn't have a parameter named forward, it'll default to '' - the empty string.
    forward = request.args.get('forward', '')
    # Python code to generate the backward version of the string and store it in a variable named backward.
    # The details of this aren't important for understanding Flask handlers.
    backward = ''.join(reversed(forward))
    # Render the reverse_result.html template using our forward variable for the template's forward variable,
    # and our backward variable for the template's backward variable.
    return render_template('grade_4_quiz.html', forward=forward, backward=backward)

app.run()
