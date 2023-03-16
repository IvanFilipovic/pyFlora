from django.core.management.base import BaseCommand
from pyflora_app.models import Stats, Pot
import random

class Command(BaseCommand):
	help = 'Fake stats'

	def handle(self, *args, **kwargs):
            pots = Pot.objects.values('id').count()
            a = Pot.objects.all()
            pots_id = a.values_list('id', flat=True)

            for id in range(pots):
                Stats.objects.create(humidity_status= random.randrange(40, 100), lux_status=random.randrange(2000, 4500), temp_status=random.randrange(15,35), ph=random.randrange(3, 9), pot_senzors_id=pots_id[id])
