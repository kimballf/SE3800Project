"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import Account

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def adduser(request):
    a = Account(username=request.POST['username'], email=request.POST['email'])
    a.save()
    return render(
        request,
        'app/adduser.html',
        context_instance = RequestContext(request,
        {
            'title':'Added User',
            'message':'Success!',
            'year':datetime.now().year,
        })
    )

def userlist(request):
    user_list = []
    for a in Account.objects.all():
        user_list.append(a.username)
    return render(
        request,
        'app/userlist.html',
        context_instance = RequestContext(request,
        {
            'title':'User List',
            'message':'The list of users',
            'user_list':user_list,
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
