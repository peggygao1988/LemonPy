# LemonPy
LemonPy is a lightweighted, flexible and intuitive web framework for Python building on CherryPy, Elixir, SQLAlchemy, JinJa2 and uwsgi.
# Introduction
LemonPy aims at provding a simple, efficient and practical web framework for Python. LemonPy composes of several open source module including:
+ CherryPy-3.6.0  A MVC web framework supporting wsgi protocol
+ JinJa2-2.7.3  A modern and designer-friendly templating language for Python
+ SQLAlchemy-1.0.0  A ORM framework for Python and a Python SQL toolkit
+ Elixir-0.7.1  A fairly thin wrapper above SQLAlchemy to create Python classes mapped to database tables. Since it is out of maintenance, I offer a version on github of [Elixir](https://github.com/peggygao1988/elixir) which is compatible to SQLAlchemy-1.0.0
+ uswgi-2.0.10 A high-performance application server for Python and process manager

# Get Started
+ lemon.ini is the config file for uwsgi. Start application server by command uwsgi --ini lemon.ini. The default mode is unix socket so you should start a Nginx or any other proxy server supporting wsgi protocol befor uwsgi app servier. wsgi_test.py is the entrance for the wsgi application.
+ According to the MVC pattern, model package contains all the python classes mapped to database table and relevant database operations.
+ The cntroller package contains the controller part in MVC pattern, connecting the views and models.
+ All views are JinJa2 templates in folder temlpate.
