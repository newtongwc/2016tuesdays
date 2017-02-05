from flask import Flask
app = Flask(_name_)
@app.route("/")
def FanFic():
    return app.send_static_file('FanFiction.html')

app.run()
