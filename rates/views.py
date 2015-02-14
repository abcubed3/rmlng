from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Rating
from .forms import RatingForm
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
   
def addRating(request, slug):
    try:
        lect = Lecturer.objects.get(slug=slug)
    except Lecturer.DoesNotExist:
        pass
    except:
        pass
    rate = Rating(rating =4.5, lecturer= lect, helpfulness="3", knowlegdeable="3", clarity="3", hotness="2", handout="2", course="EEG505", recommend="4", describe = "Description")
    rate.save()
    return HttpResponseRedirect(reverse('rates:allRatings'))
    
#def addRating(request, slug):
#    #try:
#    #    lect = Lecturer.objects.get(slug=slug)
#    #except Lecturer.DoesNotExist:
#    #    pass
#    #except:
#    #    pass
#    form = RatingForm(request.POST or None)
#    if form.is_valid():
#        save_it = form.save(commit=False)
#        save_it.save()
#        
#    return HttpResponseRedirect(reverse("ratelecturer"))
    
def ratelecturer(request, slug):
    slug = slug
    try:
        lect = Lecturer.objects.get(slug=slug)
    except Lecturer.DoesNotExist:
        pass
    except:
        pass
    rates = Rating.objects.all().filter(lecturer=lect)
    counter = Rating.objects.filter(lecturer=lect).filter(helpfulness=5).count()
    context =  {'rates': rates, 'counter':counter}
    template = 'rates/rating.html'
    return render(request, template, context)
    