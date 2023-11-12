from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = {'user1': 'password1', 'user2': 'password2'}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login, you can redirect to a dashboard or any other page
        return redirect(url_for('dashboard'))
    else:
        # Failed login, you can display an error message on the login page
        return render_template('login.html', error='Invalid username or password')


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'


if __name__ == '__main__':
    app.run(debug=True)
