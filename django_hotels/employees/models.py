from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from hotels.models import Hotel


# Create your models here.


class Employee(models.Model):
    JOB_TITLES = [
        ('bellhop', 'Bellhop'),
        ('housekeeping', 'Housekeeping'),
        ('security', 'Security'),
        ('frontdesk', 'Front Desk'),
        ('manager', 'Manager')
    ]
    user = models.OneToOneField(User, related_name='employee')
    wage = models.DecimalField(decimal_places=2, max_digits=5)
    title = models.CharField(max_length=30, choices=JOB_TITLES)
    phone_number = models.CharField(max_length=20)
    employee_id = models.UUIDField(default=uuid.uuid4, editable=False)
    currently_employed = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel, related_name='employees')


@receiver(post_save, sender=User)
def attach_employee(instance, **kwargs):
    if kwargs['created']:
        employee = Employee(
            user=instance,
            wage=15.00,
            title='frontdesk',
            hotel=Hotel.objects.first()
        )
        employee.save()
