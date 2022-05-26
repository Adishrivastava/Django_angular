from django.urls import include, path
from rest_framework import routers
from app.views import AngularViewSet


urlpatterns = [
    path('', AngularViewSet.as_view(), name="main"),
]