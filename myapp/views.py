import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.template import loader
#from myapp.form import StuForm

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from myapp.functions.functions import handle_uploaded_file
from myapp.form import StudentForm


def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request, "formUpload.html", {'form': student})
