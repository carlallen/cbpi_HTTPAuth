from modules import app, cbpi
from flask_basicauth import BasicAuth
def auth_password():
  password = cbpi.get_config_parameter('auth_password', None)
  if password is None:
    cbpi.add_config_parameter("auth_password", "password", "text", "HTTP Auth password")
    return "password"
  else:
    return password

basic_auth = BasicAuth(app)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = auth_password()
app.config['BASIC_AUTH_FORCE'] = True
