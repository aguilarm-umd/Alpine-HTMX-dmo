
# Create your views here.
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'alpine_htmx_demo/index.html')
    # return HttpResponse("Hello, world!")

def replace(request):
    return HttpResponse('<p>HTML Replaced!</p>')

def swap(request):
    pass

def send_message(request: HttpRequest) -> HttpResponse:
    """Just sends an OK message back to the user."""
    messages.success(request, "All OK!")
    return render(request, "_send_button.html", {"message_sent": True})

