import time
import logging
import logging.config
import cherrypy
import yaml

from uwsgidecorators import postfork
from controller.root import RootController
from controller.user import UserController


error_logger = logging.getLogger('error')
root = RootController()
user = UserController()
root.user = user

def handle_error():
    cherrypy.response.status = 500
    cherrypy.response.body = ["<html><body>Sorry, an error occured</body></html>"]

config = {
    '/': {
        'tool.sessions.on': True,
        'tool.sessions.timeout': 20,  # 20 minutes
        'request.show_tracebacks': False,
        'request.error_response': handle_error
    }
}


@postfork
def close_session():
    '''
        close db session after uswgi fork slave process
        lazy initialize db session when requests arrive
        then every process will own a db connection itself
    '''
    from model import session
    session.close()


def application(environ, start_response):
    cherrypy.tree.mount(root,  '/', config=config)
    response = cherrypy.tree(environ, start_response)
    return response
