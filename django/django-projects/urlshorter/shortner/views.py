from django.http import HttpResponse
from .models import Url
import uuid
from django.shortcuts import render

# Create your views here.



def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def create(request):

    if request.method == "POST":

        link = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()

        return HttpResponse(uid)
