from flask import request 
from functools import wraps

def validate_user(func):

  @wraps(func)
  def decorated_function(*args, **kwargs):
      decoded_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7Im5hbWUiOiJzZXlpIiwicGFzc3dvcmQiOiJhMWIyYzNkNGU1In0sImV4cCI6MTU2NTY5ODQ4Nn0.aP3QZgtBwWP8xrvsciUBUqSDPtII_tki2AX5O4QQ97U'
      # return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7Im5hbWUiOiJzZXlpIiwicGFzc3dvcmQiOiJhMWIyYzNkNGU1In0sImV4cCI6MTU2NTY5ODQ4Nn0.aP3QZgtBwWP8xrvsciUBUqSDPtII_tki2AX5O4QQ97U'
      setattr(request, 'decoded_token', decoded_token)
      print(request.decoded_token)
      # print(decoded_token)
      return func(*args, **kwargs)

  return decorated_function

def token_required(func):
  """ validate that a user is authenticated """
  @wraps
  def wrapper():
    auth = request.authorization
        print(auth)

        if auth and auth.password == 'a1b2c3d4e5':
            token = jwt.encode({
                'user': {'name': auth.username, 'password': auth.password},
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                os.getenv('SECRET_KEY')
            )
            return {'token': token.decode('UTF-8')}

        return make_response('could not verify', 401, {'www-authenticate': 'Basic loing reqire'})
        # return 'could not veryfi'

