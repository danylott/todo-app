from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=250, blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
