from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    if "https" in reg_val:
        new_value = reg_val
    else:
        new_value = 'https://' + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL for this field")
    return new_value


def validate_dot_com(value):
    if not 'com' in value:
        raise ValidationError('This is not a valid url')
    return value