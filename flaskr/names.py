from flask import (Blueprint, render_template)
from flaskr.db import get_db

bp = Blueprint('names', __name__, url_prefix='/names')


@bp.route('/')
def names_count():
    db = get_db()
    names = db.execute(
        'SELECT COUNT(DISTINCT artist) FROM tracks').fetchone()[0]
    return render_template('names.html', names=names)
