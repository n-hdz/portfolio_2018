from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def job(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        raise Http404('Job not found')
    return render(request, 'jobs/job_detail.html', {'job':job})
