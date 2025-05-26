from django.db import models



class Breed(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class SpyCat(models.Model):
    name = models.CharField(max_length=30)
    years_of_experience = models.IntegerField(null=True, blank=False)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, related_name='spy_cats')
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.breed}"
