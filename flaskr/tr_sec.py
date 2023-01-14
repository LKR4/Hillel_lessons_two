from flask import (Blueprint, render_template)
from flaskr.db import get_db

bp = Blueprint('tracks_sec', __name__, url_prefix='/tracks-sec')


@bp.route('/')
def track_sec():
    db = get_db()
    tracksec = db.execute(
        'SELECT title, length FROM tracks').fetchall()
    return render_template('tr_sec.html', track_sec=tracksec)


@bp.route('/statistics')
def statistic():
    db = get_db()
    all_len = db.execute('select SUM(length) from tracks').fetchone()[0]
    count = db.execute('select AVG(length) from tracks').fetchone()[0]
    return render_template('tr_stats.html', midlen=count, alllen=all_len)
