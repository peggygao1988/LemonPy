import logging
import logging.config
import cherrypy
import yaml

from uwsgidecorators import postfork
from controller.root import RootController
from controller.user import UserController

# config logging
#with open('config/log.yml') as log_config:
#    logging.config.dictConfig(yaml.load(log_config))

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
    print 'environ :', environ
    cherrypy.tree.mount(root,  '/', config=config)
    print 'url :', cherrypy.url()
    request = cherrypy.request
    print 'headers :', request.headers
    print 'header_list :', request.header_list
    print 'query_string', request.query_string
    print 'remote :', request.remote
    print 'base :', request.base
    print 'script_name :', request.script_name
    response = cherrypy.tree(environ, start_response)
    print 'response :', response
    print dir(response)
    print response.environ
    print response.response
    return response
