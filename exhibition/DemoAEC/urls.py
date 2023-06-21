from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path("demo_aec", views.show_demo_aec),
    path("show_arch", views.show_demo_arch),
    path("show_content", views.show_demo_content),
]
