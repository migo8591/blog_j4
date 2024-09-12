from flask import Flask

def create_app(config):
    app = Flask(__name__)
    @app.route('/')
    def hello():
       return "<p>Hello, World!</p>"
    return app