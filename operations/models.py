from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Barangay(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Tower(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TowerPin(models.Model):
    tower = models.OneToOneField(Tower, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    barangay = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)

    latitude = models.FloatField()
    longitude = models.FloatField()
    remarks = models.TextField(blank=True)
    picture = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tower.name} ({self.latitude}, {self.longitude})"
