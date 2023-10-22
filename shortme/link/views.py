from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from shortme.link.models import ShortMe


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'shortme/home.html', context=context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, 'shortme/home.html', context=context)


class ShortMeView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortMe, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
