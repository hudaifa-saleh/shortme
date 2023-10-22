from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from shortme.analytics.models import ClickEvent
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
        qs = ShortMe.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            return Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
