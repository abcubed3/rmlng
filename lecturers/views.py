from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, Http404

from .forms import LecturerForm
from .models import Lecturer, LecturerAttribute

from institutions.models import Institution
from django.contrib import messages
# Create your views here.


def home(request):
    
    template= 'index.html'
    return render_to_response(template, locals(), context_instance=RequestContext(request))
    #return render(request, template, context)

def lecturer(request):
    lecturers = Lecturer.objects.all()
    context =  {'lecturers': lecturers }
    template = 'lecturers/lecturers.html'
    return render(request, template, context)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q= None
    if q:
        #Search by lecturer lastName or institution name
        lecturers = Lecturer.objects.filter(lastName__icontains=q)
        institutes = Institution.objects.filter(name__icontains=q)
        if lecturers or institutes:
            context =  {'query': q, 'lecturers': lecturers, 'institutes': institutes}
            template = 'result.html'
            return render(request, template, context)
        else:
            #Search by lecturer firstName or abbrevation name
            lecturers = Lecturer.objects.filter(firstName__icontains=q)
            institutes = Institution.objects.filter(abr__icontains=q)
            if lecturers or institutes:
                context =  {'query': q, 'lecturers': lecturers, 'institutes': institutes}
                template = 'result.html'
                return render(request, template, context)
            else:
                #Search institution location
                institutes = Institution.objects.filter(location__icontains=q)
                if institutes:
                    context =  {'query': q, 'institutes': institutes}
                    template = 'result.html'
                    return render(request, template, context)
        
                else: #didnt find keyword, return to home page
                    template = 'index.html'
                    context = {'nosearch':"Didnt find your school or lecturer. Try again"}
       #No search term, user didnt enter search term
    else:
        template = 'index.html'
        context = {'nosearch':"Enter a school or lecturer in the search bar"}
    return render(request, template, context)

def seelecturer(request, slug):
    try:
        lecturer= Lecturer.objects.get(slug=slug)
        attributes = LecturerAttribute.objects.filter(lecturer=lecturer)
        context = {'lecturer': lecturer , 'attributes': attributes}
        template = 'lecturers/lecturers.html'
        return render(request, template, context)
    except:
        raise Http404
        
def addlecturer(request):
    
    form = LecturerForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Lecturer details added.')
    return render_to_response("lecturers/add-lecturer.html", locals(), context_instance=RequestContext(request))

def aboutus(request):
    
    return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

def help(request):
    
    return render_to_response("help.html", locals(), context_instance=RequestContext(request))

def contactus(request):
    
    return render_to_response("contactus.html", locals(), context_instance=RequestContext(request))