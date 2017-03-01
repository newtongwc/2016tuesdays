from flask import Flask
from flask import render_template

# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask(__name__, static_url_path='')

# Tell Flask to point users to the home page if no path is given.


@app.route("/")
def show_home_page():
    return app.send_static_file('homepage.html')

@app.route("/view_jobs_offered")
def jobs():
    list_of_jobs = [ "https://s-media-cache-ak0.pinimg.com/736x/0d/f4/5b/0df45b300b9246457dc55d4250ca2c73.jpg"
    Llama Walking]
    return render_template("view_jobs_offered.html")

@app.route("/login")
def show_login():
    return render_template('LoginMock.html')


@app.route("/signup")
def show_signup():
    return render_template('SignUpsMock.html')


if __name__ == "__main__":
    app.run()
