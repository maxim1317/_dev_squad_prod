from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request
)


app = Flask(__name__)


class User():
    """Class to manage user."""

    def __init__(self):
        "Create user."
        pass


@app.route("/policy")
def policy_view():
    return render_template('policy.html', title='Privacy policy')


@app.route('/')
def index():
    user = {'username': 'User'}
    return render_template('index.html', title='Home', user=user)


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/')
    return render_template('login.html', error=error)
