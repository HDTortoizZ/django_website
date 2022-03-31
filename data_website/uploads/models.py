from django.db import models


class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads/')
