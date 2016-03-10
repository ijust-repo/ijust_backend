# -*- coding: utf-8 -*-

# project imports
from project import app
from project.utils.validators import api_validate_schema


@app.api_route('/user/')
def get_user():
	return '1', 200


@app.api_route('/user/', methods=['POST'])
@api_validate_schema('user.signup_schema')
def signup():
	return '1', 200
