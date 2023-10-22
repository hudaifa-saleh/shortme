from django import forms
from django.core.validators import URLValidator

from shortme.link.validators import validate_dot_com, validate_url


class SubmitURL(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])

    # def clean(self):
    #     cleaned_data = super(SubmitURL, self).clean()
    #     print(cleaned_data)
    #
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL...')
    #     return url
