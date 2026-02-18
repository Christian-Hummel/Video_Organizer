from django.db import models

class Movie(models.Model):
    class Mtype(models.TextChoices):
        DVD = 'dvd', 'DVD'
        Blu = 'blu-ray', 'Blu-Ray'
    id = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=1000,null=False)
    year = models.IntegerField(null=False)
    description = models.CharField(max_length=10000,null=False)
    director = models.CharField(max_length=100,null=False)
    type = models.CharField(max_length=10, choices=Mtype.choices,default=Mtype.DVD)
    picture_description = models.CharField(max_length=100,default="",blank=True,null=True)
    picture = models.ImageField(upload_to='images/',default=0)

    def __str__(self):
        return f"{self.title} - {self.year} - {self.description} - {self.director} - {self.type}"
