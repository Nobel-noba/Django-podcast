from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


#url configration
urlpatterns = [
    path('hello/',views.hello)
]