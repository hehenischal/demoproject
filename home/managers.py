from django.db import models



class ArticleManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted=False)
