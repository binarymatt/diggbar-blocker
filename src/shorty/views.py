# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponsePermanentRedirect
from shorty.models import ShortUrl, ClickEntry
from shorty.forms import UrlForm
from utilities import string_to_integer
def redirect(request, key):
    primary_key = string_to_integer(key)
    short = get_object_or_404(ShortUrl, id=primary_key)
    entry = ClickEntry()
    entry.load_meta(request.META)
    
    entry.url = short
    entry.save()
    return HttpResponsePermanentRedirect(short.url)

def make(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            u = ShortUrl(url=url)
            u.save()
            return render_to_response('finished.html', {
                    'surl': u,
            })
    else:
        form = UrlForm()
    return render_to_response('make.html', {
            'form': form,
    })
def list(request):
    urls = ShortUrl.objects.all()
    form = UrlForm()
    context = {
        'urls': urls,
    }
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            u = ShortUrl(url=url)
            u.save()
            context['obj':u]
            form = UrlForm()
    context['form'] = form
    return render_to_response('list.html', context)