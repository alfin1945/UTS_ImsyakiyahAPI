from django.db import models

# Create your models here.
class jadwalModels (models.Model):
    tanggal = models.CharField(max_length=50)
    imsyak  = models.TimeField(auto_created=False)
    subuh   = models.TimeField(auto_created=False)
    terbit  = models.TimeField(auto_created=False)
    dhuha  = models.TimeField(auto_created=False)
    dzuhur  = models.TimeField(auto_created=False)
    asar    = models.TimeField(auto_created=False)
    magrib  = models.TimeField(auto_created=False)
    isya    = models.TimeField(auto_created=False)

    def __str__(self):
        return self.tanggal
