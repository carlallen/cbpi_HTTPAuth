from modules import app, cbpi
try:
  from flask_basicauth import BasicAuth
  basic_auth = BasicAuth(app)
except:
  import os
  os.system("pip install Flask-BasicAuth")
  cbpi.notify("HTTPAuth Error", "Flask-BasicAuth was not insalled. Restart to activate HTTPAuth", type="danger", timeout=10000)

def auth_password():
  password = cbpi.get_config_parameter('auth_password', None)
  if password is None:
    cbpi.add_config_parameter("auth_password", "password", "text", "HTTP Auth password")
    return "password"
  else:
    return password

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = auth_password()
app.config['BASIC_AUTH_FORCE'] = True
