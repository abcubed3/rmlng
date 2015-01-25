from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.
from .forms import LecturerForm
from django.contrib import messages
# Create your views here.


def home(request):
    
    #form = LecturerForm(request.POST or None)
    #if form.is_valid():
    #    save_it = form.save(commit=False)
    #    save_it.save()
    #to create a redirect
    #return HttpResponseRedirecr('/thank-you/')
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
    #return render(request, template, context)

def lecture(request):
    
    form = LecturerForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Lecturer details added.')
    return render_to_response("lecturers/lecturers.html", locals(), context_instance=RequestContext(request))

def aboutus(request):
    
    return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

def help(request):
    
    return render_to_response("help.html", locals(), context_instance=RequestContext(request))

def contactus(request):
    
    return render_to_response("contactus.html", locals(), context_instance=RequestContext(request))