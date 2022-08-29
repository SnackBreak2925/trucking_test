from django.shortcuts import render
from django.views.generic import TemplateView

# def index(request):
#     return HttpResponse("Hello, world. You're at the khhhh index.")
class Index(TemplateView):
  template_name = 'testing/main.html'
