from flask import Blueprint, render_template, request, url_for, redirect
from users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
  return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
  try:
    if request.form.get('password') != request.form.get('password_confirmation'):
      raise Exception('The password and confirmation must be the same')
    elif User.query.filter_by(email=request.form.get('email')).first():
      raise Exception('This email is already registered')
    elif len(request.form.get('password')) < 5:
      raise Exception('Password must be longer than 5 characters')

    user = User(
      email=request.form.get('email'),
      password=generate_password_hash(request.form.get('password'))
    )
    user.save()

    login_user(user)
    return redirect(url_for('index.index'))
  except Exception as error_message:
    error= error_message or 'An error occured'
    return render_template('users/register.html', error=error)


@blueprint.get('/login')
def get_login():
  return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()

    if not user:
      raise Exception('No user with the given email address was found')
    elif not check_password_hash(user.password, request.form.get('password')):
      raise Exception('The password was incorrect')
    
    login_user(user)
    return redirect(url_for('index.index'))
  except Exception as error_message:
    error=error_message or 'An error occured'
    return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
  return 'User logged out'