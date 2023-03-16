from django.shortcuts import  render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ModelFormMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from .models import *
from.forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login_process(request):
    try:
        user = authenticate(username = request.POST['username'],
            password = request.POST['password'])
    except KeyError:
        return render(request, 'loginpage.html') 
    if user is not None:
        #'User' and 'Pass' right
        if user.is_active:
            login(request, user)
        else:
            return render(request, 'loginpage.html',{
                'login_message' : 'The user has been removed',})
    else:
        return render(request, 'loginpage.html',{
            'login_message' : 'Unesite ispravno korisničko ime i/ili lozinku',})
    return HttpResponseRedirect('/dashboard')

def base(request):
	return render(request, 'base.html', {})

def dashboard(request):
    return render(request, 'base.html', {})

def addplant(request):
    return render(request, 'addplant.html', {})

def addpot(request):
    return render(request, 'addpot.html', {})

class PlantDetailView(DetailView,ModelFormMixin):
	model = Plant
	form_class = PlantForm
    
class PlantCreateView(CreateView,ModelFormMixin):
    model = Plant
    form_class = PlantForm

class PlantUpdateView(UpdateView,ModelFormMixin):
    model = Plant
    form_class = PlantForm
    success_url = '/plants'

class PlantDeleteView(DeleteView,ModelFormMixin):
    model = Plant
    form_class = PlantForm
    success_url = reverse_lazy('plant-list')

class PotCreateView(CreateView,ModelFormMixin):
    model = Pot
    form_class = PotForm
    def get_success_url(self):
        return reverse('pot-detail', kwargs={'pk': self.object.pk})

class PotUpdateView(UpdateView,ModelFormMixin):
    model = Pot
    form_class = PotForm
    success_url = '/dashboard'

class PotDeleteView(DeleteView):
    model = Pot
    success_url = reverse_lazy('dashboard')
    template_name = 'pyflora_app/pot_confirm_delete.html'

class PotDetailView(DetailView,ModelFormMixin,SingleObjectMixin):
    model = Pot
    form_class = PotForm
    related_model_name = Stats  

    def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(PotDetailView, self).get_context_data(**kwargs)
        context['stats'] = Stats.objects.filter(pot_senzors_id=self.get_object())
        return context


def humidity(request, pot_senzors_id, plant_id):
    pot_id = pot_senzors_id
    plant_id = plant_id
    labeli = []
    humidity_data = []
    queryset = Stats.objects.order_by('stats_time').filter(pot_senzors_id=pot_id, plant_id=plant_id)
    print(queryset)
    for i in queryset:
        labeli.append(i.stats_time)
        humidity_data.append(i.humidity_status)
    colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#ffeaa7', '#7082f5', '#0E27C5', '#fd79a8']
    colorPrimary = '#79aec8', colorPalette[0], colorPalette[5]
    return JsonResponse({
        'title': f'Vlažnost',
        'data': {
            'labels': labeli,
            'datasets': [{
                'label': 'Vlažnost tla / %',
                'backgroundColor': colorPalette[5],
                'borderColor': colorPalette[4],
                'data': humidity_data,
            }]
        },
    })

def lux(request, pot_senzors_id, plant_id):
    pot_id = pot_senzors_id
    plant_id = plant_id
    labeli = []
    lux_data = []
    queryset = Stats.objects.order_by('stats_time').filter(pot_senzors_id=pot_id, plant_id=plant_id)
    print(queryset)
    for i in queryset:
        labeli.append(i.stats_time)
        lux_data.append(i.lux_status)
    colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#afa91d']
    colorPrimary = '#afa91d', colorPalette[0], colorPalette[5]
    return JsonResponse({
        'title': f'Količina svijetlosti',
        'data': {
            'labels': labeli,
            'datasets': [{
                'label': 'Količina svijetlosti / cd',
                'backgroundColor': colorPrimary,
                'borderColor': colorPalette[6],
                'data': lux_data,
            }]
        },
    })

def ph(request, pot_senzors_id, plant_id):
    pot_id = pot_senzors_id
    plant_id = plant_id
    labeli = []
    ph_data = []
    queryset = Stats.objects.order_by('stats_time').filter(pot_senzors_id=pot_id, plant_id=plant_id)
    print(queryset)
    for i in queryset:
        labeli.append(i.stats_time)
        ph_data.append(i.ph)
    colorPalette = ['#174f22', '#89dd99', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8']
    colorPrimary = '#79aec8', colorPalette[0], colorPalette[5]
    return JsonResponse({
        'title': f'PH',
        'data': {
            'labels': labeli,
            'datasets': [{
                'label': 'PH tla',
                'backgroundColor': colorPalette[0],
                'borderColor': colorPalette[1],
                'data': ph_data,
            }]
        },
    })

def minerals(request, pot_senzors_id, plant_id):
    pot_id = pot_senzors_id
    plant_id = plant_id
    labeli = []
    minerals_data = []
    queryset = Stats.objects.order_by('stats_time').filter(pot_senzors_id=pot_id, plant_id=plant_id)
    print(queryset)
    for i in queryset:
        labeli.append(i.stats_time)
        minerals_data.append(i.minerals)
    colorPalette = ['#55efc4', '#81ecec', '#9c7a30', '#271f0c', '#fab1a0', '#ff7675', '#fd79a8']
    colorPrimary = '#79aec8', colorPalette[2], colorPalette[4]
    return JsonResponse({
        'title': f'Količina hranjivih tvari',
        'data': {
            'labels': labeli,
            'datasets': [{
                'label': 'Količina hranjivih tvari / ppb',
                'backgroundColor': colorPalette[2],
                'borderColor': colorPalette[3],
                'data': minerals_data,
            }]
        },
    })