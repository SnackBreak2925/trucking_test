from django.urls import path
from testing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]