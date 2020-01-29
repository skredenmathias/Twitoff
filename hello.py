from flask import Flask

app = Flask(__name)

@app.route('/')
def root():
    return('Hello, Me!')