from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="submit">
        </form>
    '''

@app.route('/logout')
def logout():
    print(session['username'])
    session.pop('username', None)
    return redirect(url_for('index'))