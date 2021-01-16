from django.urls import path, include
from .views import Propertylist, Propertydetails

app_name = 'property'

urlpatterns = [
    path('', Propertylist.as_view()),
    path('int:<pk>', Propertydetails.as_view()),
]
