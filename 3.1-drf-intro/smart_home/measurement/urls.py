from django.urls import path
from .views import sensors, measurements

urlpatterns = [
    path('sensors/', sensors, name='sensors'),
    path('sensors/<int:pk>/', sensors, name='sensors'),
    path('measurements/', measurements, name='measurements'),
]
