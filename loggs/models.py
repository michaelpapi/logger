from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Logg(models.Model):
    """A Logg which is a topic the user wants to Logg under."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        """Returning a string represeentation of our model. """
        return self.text
    

class Loggs(models.Model):
    """Specific loggs which user use to document notes under their differnt Logg"""
    logg = models.ForeignKey(Logg, related_name='logs', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'logs'

    def __str__(self):
        """Returns a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text