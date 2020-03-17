from django.db import models
from django.urls import reverse
from datetime import date

SPOTS = (
    ('M', 'Morning'),
    ('E', 'Evening'),
    ('N', 'Night')
)

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={"finch_id": self.id})
    
    def spotted_today(self):
        return self.sighting_set.filter(date=date.today()).count() >= 1

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
    