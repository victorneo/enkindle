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
              .options(joinedload('burns'))\
              .first()

    optimal = []
    total_points = s.points
    days = (s.end_date - s.start_date).days
    burn_rate = float(total_points) / days
    for day in xrange(0, days):
        optimal.append(total_points - (day * burn_rate))
    optimal.append(0.0)

    burns = []
    for b in s.burns:
        total_points -= b.points
        burns.append(total_points)

    return render_template('index.html', today=d, sprint=s, optimal=optimal, burns=burns)
