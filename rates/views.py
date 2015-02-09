from django.shortcuts import render

# Create your views here.
from .models import Rating
from lecturers.models import Lecturer

def rating(request):
    
    #return render(request, template, context)
    rates = Rating.objects.all()
    context =  {'rates': rates }
    template = 'rates/rating.html'
    return render(request, template, context)

#def get_help(request, slug):
#    counter = Rating.objects.filter(lecturer__slug=slug).filter(helpfulness=5).count()
#    context =  {'counter': counter }
#    template = 'rates/rating.html'
#    return render(request, template, context)
   


def ratelecturer(request, slug):
    slug = slug
    lect = Lecturer.objects.get(slug=slug)
    rates = Rating.objects.all().filter(lecturer=lect)
    counter = Rating.objects.filter(lecturer=lect).filter(helpfulness=5).count()
    context =  {'rates': rates, 'counter':counter}
    template = 'rates/rating.html'
    return render(request, template, context)
    