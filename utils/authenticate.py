import jwt
import datetime
import os
from flask import request 
from functools import wraps

def token_required(func):
  """ validate that a user is authenticated """
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(request.headers['Authorization'])
    auth = request.authorization

    if auth and auth.password == 'a1b2c3d4e5':
        token = jwt.encode({
            'user': {'name': auth.username, 'password': auth.password},
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            os.getenv('SECRET_KEY')
        )
        setattr(request, 'token', token.decode('UTF-8'))
        return func(*args, **kwargs)

    # return make_response('could not verify', 401, {'www-authenticate': 'Basic loing reqire'})
    # return 'could not veryfi'
  return wrapper


def assignToken(name, password):
  if name and password:
    token = jwt.encode(
      { 'name': name, 'password': password }, 
      'thisiskey').decode('UTF-8')
    return token
  else:
    print('no token')
  #   print('there  is password and username')