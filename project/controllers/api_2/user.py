# -*- coding: utf-8 -*-

# project imports
from project import app
from project.utils.validators import api_validate_schema


@app.api_route('/user/', methods=['GET', 'POST'])
@api_validate_schema('user.signup_schema')
def signup():
	return '2', 200
