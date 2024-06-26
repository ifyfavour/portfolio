from django.db import models

# Create your models here.from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

