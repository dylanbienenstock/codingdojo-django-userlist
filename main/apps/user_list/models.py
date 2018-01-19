# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
	def validate(self, first_name, last_name, email_address):
		errors = []

		email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		full_name = first_name + " " + last_name

		if len(full_name) < 2 or len(full_name) > 255:
			errors += ["Please enter a name between 2 and 255 characters."]

		if not re.match(email_regex, email_address):
			errors += ["Please enter a valid email address."]

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	objects = UserManager()