from django.forms import ModelForm
from pyflora_app.models import Plant, Pot

# Create your forms here.
class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields=['plant_name', 'plant_photo', 'plant_care_humidity', 'plant_care_light','plant_care_ph','plant_care_minerals']

class PotForm(ModelForm):
    class Meta:
        model = Pot
        fields=['pot_name', 'plants_pot']
