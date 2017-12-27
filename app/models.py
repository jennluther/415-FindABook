"""
Definition of models.
"""

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    authors = models.CharField(max_length=100, null=True, blank=True)
    average_rating = models.DecimalField(decimal_places=2, max_digits=3)
    ratings_count = models.IntegerField()
    ratings_1 = models.IntegerField()
    ratings_2 = models.IntegerField()
    ratings_3 = models.IntegerField()
    ratings_4 = models.IntegerField()
    ratings_5 = models.IntegerField()


    def __unicode__(self):
        return self.title + " by " + self.authors

class Rating(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )


    user_id = models.IntegerField()
    # book_id = models.ForeignKey('Books')
    book_id = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
    )

    rating = models.IntegerField(choices=RATING_CHOICES)
