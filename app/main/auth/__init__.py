from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='shablony')
from . import views
