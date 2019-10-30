from django.db import models

# Create your models here.
class WaveRating(models.Model):
    choices = [(0,'Bad'), (1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Excellent')]
    rating = models.IntegerField(choices = choices)
    date = models.DateTimeField('Date the rating was made')
    ip = models.CharField(max_length=15)


