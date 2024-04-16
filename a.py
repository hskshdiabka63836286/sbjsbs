from os import system
from flask import Flask


app = Flask(__name__)

@app.route('/')
def a():
  return '1'


@app.route('/aa')
def b():
  system('sudo apt install kazam')
  return 'ok'


@app.route('/bb')
def b():
  system('apt install kazam')
  return 'ok'


app.run(host="0.0.0.0")
  
