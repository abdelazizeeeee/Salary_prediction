from django.urls import path
from . import views

urlpatterns = [
    path("template/",views.index.as_view()),
    path("",views.CreateFeatures.as_view())
]
