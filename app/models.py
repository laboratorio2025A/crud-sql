from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    __tablename__ = 'TBL_SONG'
    id = db.Column('ID_SONG', db.Integer, primary_key=True)
    name = db.Column('SONG_NAME', db.String(50), nullable=False)
    path = db.Column('SONG_PATH', db.String(255), nullable=False)
    plays = db.Column('PLAYS', db.Integer, nullable=True)