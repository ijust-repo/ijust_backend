# -*- coding: utf-8 -*-

from flask import Flask


def create_app(config):
	app = Flask(config.DEFAULT_APP_NAME)
	configure_app(app, config)
	configure_extensions(app)
	append_decorators(app)
	load_schemas(app)
	return app



def configure_app(app, config, is_pyfile=False):
	if is_pyfile:
		app.config.from_pyfile(config)
	else:
		app.config.from_object(config)


def configure_extensions(app):
	from project import extensions

	for extension in extensions.__all__:
		try:
			getattr(extensions, extension).init_app(app)
		except AttributeError as e:
			print e


def append_decorators(app):
	from decorators import create_api_route
	app.api_route = create_api_route(app)


def load_schemas(app):
	from project.schemas import find_schemas
	app.schemas = find_schemas()
