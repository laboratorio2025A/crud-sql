from flask import Blueprint, request, jsonify
from .models import db, Song

song_bp = Blueprint('song_bp', __name__)

@song_bp.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'path': s.path,
        'plays': s.plays
    } for s in songs])

@song_bp.route('/songs/<int:id>', methods=['GET'])
def get_song(id):
    song = Song.query.get_or_404(id)
    return jsonify({'id': song.id, 'name': song.name, 'path': song.path, 'plays': song.plays})

@song_bp.route('/songs', methods=['POST'])
def create_song():
    data = request.get_json()
    song = Song(name=data['name'], path=data['path'], plays=data.get('plays', 0))
    db.session.add(song)
    db.session.commit()
    return jsonify({'message': 'Canción creada'}), 201

@song_bp.route('/songs/<int:id>', methods=['PUT'])
def update_song(id):
    song = Song.query.get_or_404(id)
    data = request.get_json()
    song.name = data.get('name', song.name)
    song.path = data.get('path', song.path)
    song.plays = data.get('plays', song.plays)
    db.session.commit()
    return jsonify({'message': 'Canción actualizada'})

@song_bp.route('/songs/<int:id>', methods=['DELETE'])
def delete_song(id):
    song = Song.query.get_or_404(id)
    db.session.delete(song)
    db.session.commit()
    return jsonify({'message': 'Canción eliminada'})