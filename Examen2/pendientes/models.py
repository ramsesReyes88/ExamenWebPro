from django.db import models

class Pendiente(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    user_id = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
