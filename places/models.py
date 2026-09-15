from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=100, default='Розваги')
    location = models.CharField(max_length=255, blank=True)
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def stars(self):
        return '★' * self.rating + '☆' * (5 - self.rating)

    @property
    def short_description(self):
        words = self.description.split()
        return ' '.join(words[:5]) + '...' if len(words) > 5 else self.description