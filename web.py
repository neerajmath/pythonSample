from flask import Flask
app = Flask(__name__) 

@app.route('/')
def index():  
  return 'This is Sample Python App..this is next revision'
