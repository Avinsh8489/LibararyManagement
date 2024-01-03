from django.contrib import admin
from django.urls import path, include

# App Admin
from app_admin.views import TestView, htmlTestView


urlpatterns = [
    path("test_http_response/", TestView),
    path('html_sample_code/', htmlTestView),
]