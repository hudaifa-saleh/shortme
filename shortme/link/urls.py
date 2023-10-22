from django.urls import re_path

from shortme.link.views import HomeView, ShortMeView

app_name = 'link'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^(?P<shortcode>[\w-]+)/$', ShortMeView.as_view(), name='get-link'),
]
