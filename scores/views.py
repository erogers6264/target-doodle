from django.http import HttpResponse
from django.template import loader

from .models import College

def index(request):
    top_college_list = College.objects.order_by('-SAT75pScore')[:5]
    template = loader.get_template('scores/index.html')
    context = {
        'top_college_list': top_college_list,
    }
    return HttpResponse(template.render(context, request))

def allColleges(request):
    return HttpResponse("This page will list all colleges.")

def collegeDetail(request, college_id):
    return HttpResponse("This page the detail of college %s." % college_id)
