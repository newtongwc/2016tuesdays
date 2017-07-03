from flask import Flask
from flask import render_template
from flask import request

app = Flask('States', static_url_path='')

@app.route("/")
def show_states_home():
   return app.send_static_file('states_home.html')


import random

states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware',
         'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
         'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana',
         'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada',
         'New York', 'Ohio', 'Oklahoma','Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
         'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']


@app.route("/random")
def show_random_state():
   random_state = random.choice(states)
   return render_template('states_home.html', state=random_state)

@app.route("/letter")
def show_matching_states():
   user_letter = request.args.get('user_letter', '')
   matching_states = []
   for state in states:
       if state.lower().startswith(user_letter):
           matching_states.append(state)
   output_html = ', '.join(matching_states)
   return render_template('states_home.html', user_letter=user_letter, list_of_states=output_html)

app.run()
