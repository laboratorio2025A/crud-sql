from flask import Flask
from app.config import Config
from app.models import db
from app.routes import song_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(song_bp)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')