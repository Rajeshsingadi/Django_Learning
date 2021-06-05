from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def example(request):
    try:
        text = f"<h1>This is working fine</h1>"
        fold_path = reverse('fold_name')
        return HttpResponse(text)
    except:
        return HttpResponseNotFound(f"<h1>not page</h1>")
