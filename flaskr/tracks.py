from flask import (Blueprint, render_template)
from flaskr.db import get_db

bp = Blueprint('tracks', __name__, url_prefix='/tracks')


@bp.route('/')
def tracks():
    db = get_db()
    tr = db.execute(
        'SELECT COUNT(*) FROM tracks').fetchone()[0]
    return render_template('tracks.html', tracks=tr)


@bp.route('/<genre>')
def tracks_genre(genre):
    db = get_db()
    grcount = db.execute(
        'SELECT COUNT(*) FROM tracks WHERE genre = ?', (genre,)).fetchone()[0]
    return render_template('tr_genre.html', genre=genre, count=grcount)
