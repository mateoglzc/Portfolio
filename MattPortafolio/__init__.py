from flask import Flask
from MattPortafolio.config import Config

def CreateApp(config=Config):
    
    app = Flask(__name__)
    app.config.from_object(config)

    from MattPortafolio.Main.routes import main

    app.register_blueprint(main)

    return app