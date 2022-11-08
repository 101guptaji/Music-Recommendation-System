from django.db import models

# Create your models here.
from django.db import models

from django.db.models import Avg
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=200)

    def average_rating(self):

        return 4.5


        #return self.review_set.aggreagate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    song = models.ForeignKey('song', on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField('date published')
    user_id = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    rating = models.FloatField(choices=RATING_CHOICES, default=None, null=True, blank=True)
    comment = models.CharField(max_length=200)