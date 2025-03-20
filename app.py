from flask import Flask, url_for, render_template, request
from werkzeug.utils import secure_filename

from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "hello world"

# /flask 和 /flask/ 是不同的 url，如果没有定义 /flask/，访问 /flask 会重定向到 /flask/

@app.route('/flask')
def hello_workd():
  return "hello flask"

@app.route('/flask/')
def hello_workd2():
  return "hello flask/"

@app.route('/<name>')
def hello(name):
  return f"hello, {escape(name)}12"

@app.route('/test', methods=['POST'])
def test():
  return "test"

with app.test_request_context():
  print(url_for('hello_world'))
  print(url_for('hello', name="flask"))

# static file
@app.route('/test2')
def test2():
  css_url = url_for('static', filename='index.css')
  return f'<link rel="stylesheet" href="{css_url}">Hello, World!'

# render template
@app.route('/blog')
def blog():
  return render_template('blog.html')


# request 
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    print(request.get_json())
    # print(request.form['password'])
  return "ok"

# upload
@app.route('/upload', methods=['POST'])
def upload_file():
  f = request.files['file']
  print(f.filename)
  print(f"{secure_filename(f.filename)}")
  f.save(f"uploads/{f.filename}")
  return "ok"