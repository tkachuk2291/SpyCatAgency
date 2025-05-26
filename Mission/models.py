from django.db import models



class Target(models.Model):
    mission = models.ForeignKey('Mission', on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    notes = models.TextField()
    complete_state = models.BooleanField()

class Mission(models.Model):
    cat = models.ForeignKey('spyCat.SpyCat', on_delete=models.CASCADE, related_name='missions')
    complete_state = models.BooleanField()