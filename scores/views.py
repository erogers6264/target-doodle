from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, world. You're at the scores index.")

def allColleges(request):
    return HttpResponse("This page will list all colleges.")

def collegeDetail(request, college_id):
    return HttpResponse("This page the detail of college %s." % college_id)
