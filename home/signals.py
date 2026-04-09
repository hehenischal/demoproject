from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article

@receiver(post_save, sender=Article)
def article_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Article "{instance.title}" has been created.')
    else:
        print(f'Article "{instance.title}" has been updated.')