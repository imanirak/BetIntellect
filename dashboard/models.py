from django.db import models

class Player(models.Model):
    """
   Player model for structuring sports player data.
    """
    nba_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
