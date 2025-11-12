from django.db import models
from django.contrib.auth.models import User

class Nft(models.Model):
    name = models.CharField(max_length=200)
    nft_image = models.ImageField(upload_to='image/')
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.price}"


class Collections(models.Model):
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nft.name} - {self.owner.username}"