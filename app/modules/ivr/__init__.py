"""
Create the Blueprint.
Create and import the views to be used for the Blueprint
"""
from flask import Blueprint

ivr_blueprint = Blueprint('ivr', __name__)

from . import routes
