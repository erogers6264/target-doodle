from django.http import HttpResponse
from django.template import loader

from .models import College

def index(request):
    top_college_list = College.objects.order_by('-SAT75pScore')[:5]
    context = {
        'top_college_list': top_college_list,
    }
    return render(request, 'polls/index.html', context)

def allColleges(request):
    return HttpResponse("This page will list all colleges.")

def collegeDetail(request, college_id):
    return HttpResponse("This page the detail of college %s." % college_id)
