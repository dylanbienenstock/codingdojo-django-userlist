# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User

def index(request):
	context = {
		"users": User.objects.all()
	}

	return render(request, "index.html", context)

def new(request):
	context = {
		"errors": None
	}

	return render(request, "new.html")

def new_submit(request):
	if request.method == "POST":
		first_name = request.POST["first_name"].rstrip()
		last_name = request.POST["last_name"].rstrip()
		email_address = request.POST["email_address"].rstrip()

		errors = User.objects.validate(first_name, last_name, email_address)

		if len(errors) > 0:
			context = {
				"errors": errors
			}

			return render(request, "new.html", context)

		User.objects.create(first_name=first_name, last_name=last_name, email_address=email_address)

	return redirect("/")

def show(request, id):
	context = {
		"user": User.objects.get(id=id)
	}

	return render(request, "show.html", context)

def edit(request, id):
	context = {
		"user": User.objects.get(id=id),
		"errors": []
	}

	return render(request, "edit.html", context)

def edit_submit(request, id):
	if request.method == "POST":
		first_name = request.POST["first_name"].rstrip()
		last_name = request.POST["last_name"].rstrip()
		email_address = request.POST["email_address"].rstrip()

		user = User.objects.get(id=id)
		errors = User.objects.validate(first_name, last_name, email_address)

		if len(errors) > 0:
			context = {
				"user": user,
				"errors": errors
			}

			return render(request, "edit.html", context)

		user.first_name = first_name
		user.last_name = last_name
		user.email_address = email_address
		user.save()

	return redirect("/")

def delete(request, id):
	User.objects.get(id=id).delete()

	return redirect("/")