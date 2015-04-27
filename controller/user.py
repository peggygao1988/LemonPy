import cherrypy
#import json
from root import BaseController
from model import User


class UserController(BaseController):

    @cherrypy.expose
    def add_user(self, username, password, gender, email, **kw):
        User.create_user(username, password, gender, email)
        return 'add user success'

    @cherrypy.expose
    def list_users(self, **kw):
        users = User.get_all_users()
        usernames = [user.username for user in users]
        return self._render(tmpl_name=user, usernames=usernames)
