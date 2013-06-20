# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if new_user is not None and new_user.is_active:
                login(request, new_user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('registration/register.html', {'form': form}, context_instance=RequestContext(request))