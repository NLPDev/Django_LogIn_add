from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import re

class EmailOrUsernameModelBackend(object):
	"""
	This is a ModelBacked that allows authentication with either a username or an email address.

	"""
	def authenticate(username=None, password=None):

		if len(username) > 7:
			if re.match("^.+@[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", username) != None:
				kwargs = {'email': username}
		else:
			kwargs = {'username': username}

		try:
		
			user = get_user_model().objects.get(**kwargs)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None

	def get_user(self, username):
		try:
			return get_user_model().objects.get(pk=username)
		except get_user_model().DoesNotExist:
			return None