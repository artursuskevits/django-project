from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_links = models.JSONField()  # Для хранения ссылок на фотографии
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
