from datetime import date
from flask import Blueprint, request, render_template
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from .models import Sprint


views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
def index():
    d = date.today()
    s = Sprint.query.order_by(desc(Sprint.number))\
              .options(joinedload('burns'), joinedload('milestone'))\
              .first()

    return render_template('index.html', today=d, sprint=s)
