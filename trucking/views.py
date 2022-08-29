from django.shortcuts import redirect
from django.views.generic import TemplateView

def index(request):
    return redirect('/testing/')
