from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import College

def index(request):
    top_college_list = College.objects.order_by('-SAT75pScore')[:5]
    context = {
        'top_college_list': top_college_list,
    }
    return render(request, 'scores/index.html', context)

def collegeDetail(request, college_id):
    try:
        college = College.objects.get(pk=college_id)
    except College.DoesNotExist:
        raise Http404("College does not exist")
    return render(request, 'scores/detail.html', {'college': college})

def allColleges(request):
    colleges = College.objects.all()
    return render(request, 'scores/allColleges.html', {'colleges': colleges})
