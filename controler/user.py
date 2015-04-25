import cherrypy
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))


class Root:

    def index(self, **kw):
        tmpl = env.get_template('index.html')
        return tmpl.render(name='StarPy')

class User:

    pass
