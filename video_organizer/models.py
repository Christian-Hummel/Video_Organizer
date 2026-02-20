from django.db import models

class Movie(models.Model):
    class Mtype(models.TextChoices):
        DVD = 'dvd', 'DVD'
        Blu = 'blu-ray', 'Blu-Ray'
    class Genre(models.TextChoices):
        ADVENTURE = 'abenteuer', 'Abenteuer'
        ACTION = 'action', 'Action'
        ANIMATION = 'animation', 'Animation'
        ANIME = 'anime', 'Anime'
        DOKU = 'doku', 'Doku'
        DRAMA = 'drama', 'Drama'
        FANTASY = 'fantasy', 'Fantasy'
        HORROR = 'horror', 'Horror'
        COMEDY = 'komödie', 'Komödie'
        CRIME = 'krimi', 'Krimi'
        LOVE = 'liebesfilm', 'Liebesfilm'
        MUSIC = 'musik', 'Musik'
        MUSICAL = 'musical', 'Musical'
        SCYFY = 'science-fiction', 'Science-Fiction'
        THRILLER = 'thriller', 'Thriller'
        WESTERN = 'western', 'Western'
    class View(models.TextChoices):
        YES = 'ja', 'Ja'
        NO = 'nein', 'Nein'
    id = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=1000,null=False)
    year = models.IntegerField(null=False)
    genre = models.CharField(max_length=20, choices=Genre.choices, default=Genre.ACTION)
    description = models.CharField(max_length=10000,null=False)
    director = models.CharField(max_length=100,null=False)
    runtime = models.IntegerField(null=False, default=130)
    type = models.CharField(max_length=10, choices=Mtype.choices, default=Mtype.DVD)
    viewed = models.CharField(max_length=10, choices=View.choices, default=View.NO)
    picture_description = models.CharField(max_length=100,default="",blank=True,null=True)
    picture = models.ImageField(upload_to='images/',default=0)
    
    

    def __str__(self):
        return f"{self.title} - {self.year} - {self.description} - {self.director} - {self.type}"
