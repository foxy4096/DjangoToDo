from django.db import models

# Create your models here.
class ToDo(models.Model):
    """Model definition for ToDo."""

    # TODO: Define fields here
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for ToDo."""

        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self):
        """Unicode representation of ToDo."""
        return self.title
