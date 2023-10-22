from django.urls import re_path

from shortme.link.views import ShortMeView

app_name = 'link'
urlpatterns = [
    re_path(r'link/(?P<shortcode>[\w-]){6,15}$', ShortMeView.as_view(), name='get-link'),
]