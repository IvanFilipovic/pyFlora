from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('loginpage/', views.login_process, name='loginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.base, name='base'),
    path('addplant/', views.addplant, name='addplant'),
    path('addpot/', views.addpot, name='addpot'),

    path('plant/add/', views.PlantCreateView.as_view(), name='plant-add'),
    path('plant/<int:pk>/', views.PlantUpdateView.as_view(), name='plant-update'),
    path('plantdetails/<int:pk>/', views.PlantDetailView.as_view(), name='plant-detail'),
    path('plant/<int:pk>/delete/', views.PlantDeleteView.as_view(), name='plant-delete'),

    path('pot/add/', views.PotCreateView.as_view(), name='pot-add'),
    path('pot/<int:pk>/', views.PotUpdateView.as_view(), name='pot-update'),
    path('potdetails/<int:pk>/', views.PotDetailView.as_view(), name='pot-detail'),
    path('pot/<int:pk>/delete/', views.PotDeleteView.as_view(), name='pot-delete'),
    path('chart/humidity/<int:pot_senzors_id>/<int:plant_id>', views.humidity, name='chart_humidity'),
    path('chart/lux/<int:pot_senzors_id>/<int:plant_id>', views.lux, name='chart_lux'),
    path('chart/ph/<int:pot_senzors_id>/<int:plant_id>', views.ph, name='chart_ph'),
    path('chart/minerals/<int:pot_senzors_id>/<int:plant_id>', views.minerals, name='chart_minerals'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)