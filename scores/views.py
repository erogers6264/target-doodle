from django.http import HttpResponse

from .models import College

def index(request):
    top_college_list = College.objects.order_by('-SAT75pScore')[:5]
    output = ', '.join([c.college_name + ': ' +str(c.SAT75pScore) for c in top_college_list])
    return HttpResponse(output)

def allColleges(request):
    return HttpResponse("This page will list all colleges.")

def collegeDetail(request, college_id):
    return HttpResponse("This page the detail of college %s." % college_id)
