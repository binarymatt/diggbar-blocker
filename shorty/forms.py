from django.forms import ModelForm
from shorty.models import ShortUrl
class UrlForm(ModelForm):
    class Meta:
        model = ShortUrl
    
