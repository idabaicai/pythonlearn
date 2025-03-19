from flask import Flask, url_for

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