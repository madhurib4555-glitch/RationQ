from django.db import models
from django.contrib.auth.models import User


class QueueToken(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    token_number = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
       max_length=20,
    choices=[
        ('Waiting', 'Waiting'),
        ('Completed', 'Completed')
    ],
    default='Waiting'
    )

    def __str__(self):
        return self.token_number