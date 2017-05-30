"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext, Context, Template
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import *
from django.template.loader import select_template
from app.forms import *
from app.models import *
import sqlite3
import json


def home(request):
    """Renders the home page."""
    conn = sqlite3.connect('db.sqlite3')
    #c = conn.execute("")

    


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    form = ContactForm(data=request.POST)
    if form.is_valid():
        contact_name = request.POST.get('contact_name', '')
        contact_email = request.POST.get('contact_email', '')
        form_content = request.POST.get('message', '')

        p = ContactSubmission(name = contact_name, email = contact_email, message = form_content)
        p.save()

        title = "Thank you for your interest!"
        message = "I will get back to you when I get the chance"
        return HttpResponse(json.dumps({'message': message, 'title': title}))
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/contact.html',
            {
                'title':'Contact',
                'message':'Your contact page.',
                'year':datetime.now().year,
                'form': ContactForm,
            }
        )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin(request):

    path = list(filter(None, request.path.split("/")))
    
    if len(path) > 1:
        pageName = path[1].lower()
        template = select_template(['app/admin/' + pageName + '.html', 'app/404.html'])
        assert isinstance(request, HttpRequest)

        if pageName == 'contacts':
            query_results = ContactSubmission.objects.all()
            context = { 'title':'Contact List',
                        'message':'This is a list of contacts',
                        'year':datetime.now().year,
                        'results':query_results,
                      }
        elif pageName == 'pagelist':
            context = { 'title':'Page List',
                        'message':'This is a list of pages',
                        'year':datetime.now().year,
                        'form': PageDetailsForm,
                      }
        else:
            context = { 'title':'Admin',
                        'message':'this is the main admin page.',
                        'year':datetime.now().year,
                      }
        
        return HttpResponse(template.render(context, request))
    elif len(path) == 0:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/admin/globalSettings.html',
            {
                'title':'Admin',
                'message':'this is the main admin page.',
                'year':datetime.now().year,
            }
        )
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/admin/globalSettings.html',
            {
                'title':'Admin',
                'message':'this is the main admin page.',
                'year':datetime.now().year,
                
            }
        )