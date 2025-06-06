from django.db import models



class SpyCat(models.Model):
    name = models.CharField(max_length=30)
    years_of_experience = models.IntegerField(null=True, blank=False)
    breed = models.CharField(max_length=30 , unique=True)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.breed}"
