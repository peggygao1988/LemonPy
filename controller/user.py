import cherrypy
import json
from jinja2 import Environment, FileSystemLoader
from model import User

env = Environment(loader=FileSystemLoader('template'))


class RootController:

    @cherrypy.expose
    def index(self, **kw):
        tmpl = env.get_template('index.html')
        return tmpl.render(name='LemonPy')


class UserController:

    @cherrypy.expose
    def add_user(self, username, password, gender, email, **kw):
        User.create_user(username, password, gender, email)
        return 'add user success'

    @cherrypy.expose
    def list_users(self, **kw):
        users = User.get_all_users()
        usernames = [user.username for user in users]
        return json.dumps(usernames)
