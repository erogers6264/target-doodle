from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import College

def index(request):
    top_college_list = College.objects.order_by('-SAT75pScore')[:5]
    context = {
        'top_college_list': top_college_list,
    }
    return render(request, 'scores/index.html', context)

def collegeDetail(request, college_id):
    college = get_object_or_404(College, pk=college_id)
    return render(request, 'scores/detail.html', {'college': college})

def allColleges(request):
    colleges = College.objects.all()
    return render(request, 'scores/allColleges.html', {'colleges': colleges})
