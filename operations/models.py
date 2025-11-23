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
    
    
from django.contrib.auth.models import User
from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
# other imports...
class TowerPin(models.Model):

    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Rescheduled", "Rescheduled"),
        ("Surveyed", "Surveyed"),
        ("On Going Construction", "On Going Construction"),
        ("Instrumentation", "Instrumentation"),
        ("Completed", "Completed"),
        ("Up and Running", "Up and Running"),
        ("For Repair", "For Repair"),
        ("Up but Standby", "Up but Standby"),
    ]

    tower = models.OneToOneField(Tower, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    barangay = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)

    latitude = models.FloatField()
    longitude = models.FloatField()
    contact = models.CharField(max_length=250, null=True, blank=True)
    remarks = models.TextField(blank=True)
    picture = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')
    picture1 = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')


    contruction_remarks = models.TextField(blank=True)
    construction_picture = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')
    construction_picture1 = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')

    instrumentation_remarks = models.TextField(blank=True)
    instrumentation_picture = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')
    instrumentation_picture1 = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='SIMOS/')
    technical_notes = models.TextField(blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Surveyed"
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.province.name} - {self.tower.name} "

