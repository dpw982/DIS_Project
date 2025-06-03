from flask import Blueprint, render_template
from ..models import University

# Renders html pages at a given route


main_bp = Blueprint('main', __name__)

# Index / home page
@main_bp.route('/')
def index():
    return render_template('index.html')

# Curriculum page
@main_bp.route('/curriculum')
def curriculum():
    return render_template('curriculum.html', active_page='curriculum')
