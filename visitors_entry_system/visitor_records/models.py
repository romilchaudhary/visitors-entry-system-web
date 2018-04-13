from ..base.models import UUIDModel
from django.db import models


class VisitorDetail(UUIDModel, models.Model):
    """
    model for storing vistors check-in
    checkout time and details
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile_number = models.IntegerField(default=0)
    details = models.TextField()
    entry_time = models.DateTimeField(auto_now=True)
    exit_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Visitor Detail'
        verbose_name_plural = 'Visitors Details'
