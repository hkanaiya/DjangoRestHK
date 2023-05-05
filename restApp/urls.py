from django.urls import path
from .views import MyModelList

urlpatterns = [
    path('', MyModelList.as_view()),
    path('mymodels/', MyModelList.as_view()),
]