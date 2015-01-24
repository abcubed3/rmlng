from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.
from .forms import InstitutionForm

# Create your views here.


def home(request):
    
    form = InstitutionForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = "Your institution has been added"
        from_email = settings.EMAIL_HOST_USER
        message = 'Your institution has been noted. But would like you to provide some more insight about the school, to help us improve users experience.'
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, 'Schools details added.')
    return render_to_response("schools.html", locals(), context_instance=RequestContext(request))


def topschools(request):
    
    
    return render_to_response("top-schools.html", locals(), context_instance=RequestContext(request))
