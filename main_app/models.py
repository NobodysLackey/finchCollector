from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SPOTS = (
    ('M', 'Morning'),
    ('E', 'Evening'),
    ('N', 'Night')
)

class Feather(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('feathers_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    feathers = models.ManyToManyField(Feather)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={"finch_id": self.id})
    
    def spotted_today(self):
        return self.sighting_set.filter(date=date.today()).count() > 0

class Photo(models.Model):
  url = models.CharField(max_length=200)
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  def __str__(self):
      return f"Photo for finch_id: {self.finch_id} @{self.url}"

class Sighting(models.Model):
    date = models.DateField('sighting date')
    spot = models.CharField(
        max_length=1,
        choices=SPOTS,
        default=SPOTS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_spot_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
