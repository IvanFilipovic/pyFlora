from rest_framework import status
from rest_framework.response import Response
from pyflora_app.models import Pot, Plant, Stats
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from api.serializers import *
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.db.utils import OperationalError
from django.core.exceptions import ObjectDoesNotExist

class PotList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    def get(self, request):
        pot_data = Pot.objects.all().select_related(
            'plants_pot',
        )
        context = {'pots':pot_data}
        return Response(context)

class PlantsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'plants.html'

    def get(self, request):
        plant_data = Plant.objects.all()
        context = {'plants':plant_data}
        return Response(context)

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class StatsCreateView(CreateAPIView, CreateModelMixin):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StatsSerializer
    queryset = Stats.objects.all()
    permission_classes = [AllowAny]

class PotListId(ListAPIView, ListModelMixin):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = PotSerializer
    queryset = Pot.objects.filter(plants_pot_id__isnull=False)

class StatsList(RetrieveAPIView, RetrieveModelMixin):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StatusSerializer
    try:
        queryset = Stats.objects.all().latest('stats_time')
    except OperationalError and ObjectDoesNotExist:
        pass
    
    def get_object(self, queryset=None): 
        pot = self.kwargs.get('pot_senzors_id')
        plant = self.kwargs.get('plant_id')
        obj = Stats.objects.filter(pot_senzors_id=pot, plant_id=plant).latest('stats_time')
        return obj