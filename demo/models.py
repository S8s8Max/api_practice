from django.db import models

# Create your models here.
class Data(models.Model):
    class Meta:
        db_table = 'interest_rate'

    year = models.CharField(verbose_name="year",max_length=20,)
    country = models.TextField(verbose_name="country",max_length=100,)
    interest_rate = models.FloatField(verbose_name="interest_rate",blank=True,null=True)

    def __str__(self):
        name = country + "_" + year
        return self.name
