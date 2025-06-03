from flask import Blueprint, jsonify
from ..models import User

# This file defines the routes for the users API

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def get_users():
  users = User.query.all()
  return jsonify([user.to_dict() for user in users])
