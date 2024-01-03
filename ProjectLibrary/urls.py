from django.contrib import admin
from django.urls import path, include

# App Admin
# from app_admin.views import TestView
# from app_admin import views

urlpatterns = [
    path('admin_panel/', admin.site.urls),

    # You can define the app url / end point in project url
    # path(route ="test_http_response/", view= TestView),
    # path("test_http_response/", views.TestView)

    # App Admin 
    path("admin/", include("app_admin.urls")),

    # Books 
    path("books/", include("books.urls")),
]
