import cherrypy
from uwsgidecorators import postfork
from controller.root import RootController
from controller.user import UserController

root = RootController()
user = UserController()
root.user = user

config = {
    '/': {
        'tool.sessions.on': True,
        'tool.sessions.timeout': 20,  # 20 minutes
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
    return cherrypy.tree(environ, start_response)
