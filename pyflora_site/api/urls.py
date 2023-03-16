from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.PotList.as_view(), name='dashboard'),
    path('plants', views.PlantsList.as_view(), name='plants'),
    path('stats', views.StatsCreateView.as_view(), name='stats'),
    path('potlist', views.PotListId.as_view(), name='potlist'),
    path('plantinpotstatus/<int:pot_senzors_id>/<int:plant_id>', views.StatsList.as_view(), name='plantinpotstatus'),
]
