import logging
import cherrypy
from jinja2 import Environment, FileSystemLoader
import globals

logger = logging.getLogger('root')
env = Environment(loader=FileSystemLoader('template'))


class BaseController:

    def _render(self, tmpl_name, **kw):
        #tmpl_name = kw.get(tmpl_name, 'index')
        tmpl = env.get_template('.'.join([tmpl_name, 'html']))
        return tmpl.render(**kw)


class RootController(BaseController):

    @cherrypy.expose
    def index(self, **kw):
        logger.info('welcome to lemonpy homepage...')
        raise KeyError('error for test')
        return self._render(tmpl_name='index', name='LemonPy')
