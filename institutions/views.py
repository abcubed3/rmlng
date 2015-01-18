from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.
from .forms import InstitutionForm
from django.contrib import messages
# Create your views here.


def home(request):
    
    form = InstitutionForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Schools details added.')
    return render_to_response("schools.html", locals(), context_instance=RequestContext(request))
