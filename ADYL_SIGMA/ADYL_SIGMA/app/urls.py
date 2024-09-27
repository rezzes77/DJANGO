from django.urls import path
from . views import CarViewset

urlpatterns = [
    path('car/', CarViewset.as_view({'get': 'list'}), name = 'cars'),
]