from django.db import models

from shortme.link.models import ShortMe


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortMe):
            obj, created = self.get_or_create(shortme_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    shortme_url = models.OneToOneField(ShortMe, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
