from django.db.models.signals import pre_delete, pre_save, post_save

from django.dispatch import receiver
from .models import Health


# @receiver(post_save, sender=Health)
# def post_save_update(sender, instance, **kwargs):
#     default_value = sender.objects.get(pk=instance.id)
#     if default_value.file == '':
#         set_value(default_value)

