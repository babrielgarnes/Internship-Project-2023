from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    max_players = models.IntegerField(null=True)
    time = models.IntegerField(null=True)
    owner = models.CharField(max_length=255, null=True, default='No owner specified')
    desc = models.CharField(max_length=255, null=True, default='No description given')

    def __str__(self):
        return f"{self.name}"
