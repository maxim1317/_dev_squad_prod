from flask import Flask 
from flask import render_template
  
app = Flask(__name__) 
  
@app.route("/") 
@app.route("/index")
def home_view():
	user = {'username': 'User'}
	return render_template('index.html', title='Home', user=user)

@app.route("/") 
@app.route("/policy")
def policy_view():
	return render_template('policy.html', title='Privacy policy')