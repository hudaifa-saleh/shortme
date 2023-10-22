from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from shortme.link.forms import SubmitURL
from shortme.link.models import ShortMe


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitURL()
        context = {'form': form}
        return render(request, 'shortme/home.html', context=context)

    def post(self, request, *args, **kwargs):
        form = SubmitURL(request.POST)
        context = {'form': form}
        template = 'shortme/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = ShortMe.objects.get_or_create(url=new_url)
            context = {'created': created, 'object': obj}
            if created:
                template = 'shortme/success.html'
            else:
                template = 'shortme/already_exists.html'
        return render(request, template, context)


class ShortMeView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortMe, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
