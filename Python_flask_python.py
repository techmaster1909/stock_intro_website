from flask import Flask, render_template
app = Flask('app')

import gevent.pywsgi
host = '0.0.0.0'
port = 8080
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/Long_Trade.html')
def long_trades():
  return render_template("Long_Trades.html")
@app.route('/Short_Trades.html')  
def short_trades():
  return render_template("Short_Trades.html")

app_server = gevent.pywsgi.WSGIServer((host , port ), app)

app_server.serve_forever()
