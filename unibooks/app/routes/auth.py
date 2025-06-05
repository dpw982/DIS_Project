from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import User, db
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import or_

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    if User.query.filter((User.username == username) | (User.email == email)).first():
      flash('Username or email already exists', 'error')
      return redirect(url_for('auth.signup'))
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return render_template('signup.html')
  return render_template('signup.html')
  
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    identifier = request.form['username']
    password = request.form['password']
    user = User.query.filter(
      or_(User.username == identifier, User.email == identifier)).first()
    if user and user.check_password(password):
      login_user(user)
      return redirect(url_for('main.index'))
    else:
      flash('Invalid username or password', 'error')
      return redirect(url_for('auth.login'))
  return render_template('login.html')
  
@auth_bp.route('/logout')
@login_required
def logout():
  logout_user()
  return render_template('logout.html')