from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Feather, Photo
from .forms import SightingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'finchcollector3'

def add_photo(request, finch_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, finch_id=finch_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'species', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feathers_finch_doesnt_have = Feather.objects.exclude(id__in = finch.feathers.all().values_list('id'))
  sighting_form = SightingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch,
    'sighting_form': sighting_form,
    'feathers': feathers_finch_doesnt_have
  })

def add_sighting(request, finch_id):
  form = SightingForm(request.POST)
  if form.is_valid():
    new_sighting = form.save(commit=False)
    new_sighting.finch_id = finch_id
    new_sighting.save()
  return redirect('detail', finch_id=finch_id)

def assoc_feather(request, finch_id, feather_id):
  Finch.objects.get(id=finch_id).feathers.add(feather_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_feather(request, finch_id, feather_id):
  Finch.objects.get(id=finch_id).feathers.remove(feather_id)
  return redirect('detail', finch_id=finch_id)

class FeatherList(ListView):
  model = Feather

class FeatherDetail(DetailView):
  model = Feather

class FeatherCreate(CreateView):
  model = Feather
  fields = '__all__'

class FeatherUpdate(UpdateView):
  model = Feather
  fields = ['name', 'color']

class FeatherDelete(DeleteView):
  model = Feather
  success_url = '/feathers/'