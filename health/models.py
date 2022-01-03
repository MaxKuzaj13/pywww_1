from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


def validate_data():
    return (MinValueValidator(1), MaxValueValidator(300))

class Health(models.Model):
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE,)
    systolic_blood_pressure = models.PositiveSmallIntegerField(validators=validate_data())
    diastolic_blood_pressure  = models.PositiveSmallIntegerField(validators=validate_data())
    pulse = models.PositiveSmallIntegerField(validators=validate_data())
    glucose = models.PositiveSmallIntegerField(validators=validate_data())
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Zdrowie"
        verbose_name_plural = "Zdrowie"
