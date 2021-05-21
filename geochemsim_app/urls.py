from django.urls import path

from . import views

app_name = "geochemsim_app"
urlpatterns = [
    path('supcrtbl2', views.supcrtbl2, name="supcrtbl2")
]
