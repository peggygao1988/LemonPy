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
        user_list = [{'username': user.username, 'email': user.email} for user
                     in users]
        return self._render(tmpl_name='user', users=user_list)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def search_users(self, key, **kw):
        users = User.search_user_by_username(key)
        user_list = [user.username for user in users]
        return dict(ret=1, data=user_list)
