from .views import home
from django.urls import path, include

app_name = "core"
urlpatterns = [
    path("", home, name='home'),
]
