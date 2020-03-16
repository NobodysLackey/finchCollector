from django.shortcuts import render
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

finches = [
  Finch('Tweety', 'Saffron Finch', 'Golden yellow', 3),
  Finch('Barry', 'Strawberry Finch', 'Deep red and maroon with white spots', 0),
  Finch('Rainbow', 'Gouldian Finch', 'Bright red, cyan, violet, green, and gold', 4)
]

def home(request):
  return HttpResponse('<h1>Hello Finch</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})