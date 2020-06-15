from flask import Blueprint

main = Blueprint('main', __name__, template_folder='shablony')

from . import views
