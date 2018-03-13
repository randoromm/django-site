from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home/$', views.home, name="home"),
    url(r'^p5js/', views.p5js, name="p5js"),
    url(r'^contact/', views.p5js, name="contact")
]
