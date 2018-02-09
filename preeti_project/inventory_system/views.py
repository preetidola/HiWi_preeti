# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from inventory_system.forms import Login
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    template = loader.get_template('inventory_system/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def log(request):
    if request.method == 'POST':
        template = loader.get_template('inventory_system/login.html')
        form = Login(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['uid']
            passwd = form.cleaned_data['pwd']
            user = authenticate(username=uid, password=passwd)
            if user is not None:
                print user 
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                template = loader.get_template('inventory_system/login.html')
                context = {
                'form': form,
                }
                return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('inventory_system/login.html')
            context = {
            'form': form,
            }
            return HttpResponse(template.render(context, request))
   
    else:
        template = loader.get_template('inventory_system/login.html')
        form = Login()
        context = {
        'form' : form,
        }
        return HttpResponse(template.render(context, request))    

def home(request):
    template = loader.get_template('inventory_system/home.html')
    context = {}
    return HttpResponse(template.render(context, request))
