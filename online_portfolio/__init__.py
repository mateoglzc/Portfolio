from flask import Flask
from online_portfolio.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from online_portfolio.Main.routes import main

    app.register_blueprint(main)
    
    return app