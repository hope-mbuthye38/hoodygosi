from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class estatedomin(models.Model):

    location = models.CharField(max_length=100)
    image = models.ImageField( upload_to='profile_pics', default='default.jpg')
    description = models.TextField()
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('estatedomin-detail', kwargs={'pk': self.pk})

class News(models.Model):
    tag = models.CharField(max_length=100)
    cation = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    estatedomin = models.ForeignKey(estatedomin, related_name='news', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('estatedomain-detail', args={self.kijiji.id})

class Business(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    contacts = models.CharField(max_length=11)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    estatedomin = models.ForeignKey(estatedomin, related_name='business', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('estatedetail', args={self.estatedomin.id})

class Police(models.Model):
    station = models.CharField(max_length=100)
    contacts = models.CharField(max_length=11)
    estatedomin= models.ForeignKey(estatedomin, related_name='police', on_delete=models.CASCADE)

    def __str__(self):
        return self.station

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=11)
    estatedomin= models.ForeignKey(estatedomin, related_name='hospital', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile_pics', default='default.jpg')
    bio = models.TextField()
    estatedomin= models.ForeignKey(estatedomin, related_name='profile')


    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('estatedetail', args={self.estatedomin.id})