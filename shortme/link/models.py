from django.conf import settings
from django.db import models
from django_hosts.resolvers import reverse

from shortme.link.validators import validate_dot_com, validate_url
from .utils import create_shortcode

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class ShortMeManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortMeManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    @staticmethod
    def refresh_shortcodes(items=None):
        qs = ShortMe.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(f'{q.shortcode} | {q.id}')
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class ShortMe(models.Model):
    url = models.CharField(max_length=250, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = ShortMeManager()

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortMe, self).save(*args, **kwargs)

    def get_short_url(self):
        url_path = reverse("links:get-link", kwargs={'shortcode': self.shortcode}, host='www', scheme='https')
        return url_path
