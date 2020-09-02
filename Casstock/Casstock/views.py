from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def login(req):

    return render(req, "login.html")

def dashboard(req):

    return render(req, "dashboard.html")