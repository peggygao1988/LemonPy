import time
import logging
import logging.config
import cherrypy
import yaml

from uwsgidecorators import postfork
from controller.root import RootController
from controller.user import UserController

# config logging
# with open('config/log.yml') as log_config:
#    logging.config.dictConfig(yaml.load(log_config))
error_logger = logging.getLogger('error')
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


def _on_internal_error(env):
    tb = cherrypy._cperror.format_exc()
    url = env['PATH_INFO'] + env['QUERY_STRING']
    ip = env['REMOTE_ADDR']
    message = '"{}" "{}" "{}"'.format(ip, url, tb)
    error_logger.error(message)
    cherrypy.HTTPError(500).set_response()
    cherrypy.response.finalize()
    response = cherrypy._cprequest.Response()
    response.status = "500 server internal error"
    response.header_list = [('Content-Type', 'text/plain'), ('Content-Length', '25')]
    response.body = "Oooooops, Server Internal Error"
    return response


def application(environ, start_response):
    cherrypy.tree.mount(root,  '/', config=config)
    try:
        response = cherrypy.tree(environ, start_response)

    except Exception, e:
        response = _on_internal_error(environ)

    return response
