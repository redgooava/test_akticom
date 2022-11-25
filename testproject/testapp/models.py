from django.db import models


class CSVModel(models.Model):
    code = models.CharField(blank=True, max_length=25500)
    name = models.CharField(blank=True, max_length=25500)
    lvl1 = models.CharField(blank=True, max_length=25500)
    lvl2 = models.CharField(blank=True, max_length=25500)
    lvl3 = models.CharField(blank=True, max_length=25500)
    price = models.CharField(blank=True, max_length=25500)
    priceSP = models.CharField(blank=True, max_length=25500)
    amount = models.CharField(blank=True, max_length=25500)
    propertyFields = models.CharField(blank=True, max_length=25500)
    purchases = models.CharField(blank=True, max_length=25500)
    unit = models.CharField(blank=True, max_length=25500)
    img = models.CharField(blank=True, max_length=25500)
    onGeneral = models.CharField(blank=True, max_length=25500)
    description = models.CharField(blank=True, max_length=25500)


class UploadCSV(models.Model):
    file = models.FileField(upload_to='files_csv/')

    def __str__(self):
        return self.file
