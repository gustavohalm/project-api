from django.db import models


class Project(models.Model):
    name = models.CharField(null=False, blank=False)
    init_date = models.DateField(null=False, blank=False)
    finished_date = models.DateField(null=False, blank=False)
