from django.conf.urls import url
from . import views  # Import from local directory

urlpatterns = [
    url(r'^$', views.index, name="index"),  # r'^&' - it begins and it ends (basically index)
]