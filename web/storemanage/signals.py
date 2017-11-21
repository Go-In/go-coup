from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from usermanage.models import Customer

@receiver(post_save, sender = Customer)
def test_handler(sender, **kwargs):
    print(sender)
    print("user created")
