from flask import Flask

# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask(__name__, static_url_path='')

# Tell Flask to point users to the home page if no path is given.
@app.route("/")
def show_home_page():
    return app.send_static_file('homepage.html')


@app.route("/Post_a_job.html")
def postJob():
    return render_template("Post_a_job.html")

if __name__ == "__main__":
    app.run()


