from django.db import models
from utilities import string_to_integer, id_to_string
import logging
class ShortUrl(models.Model):
    url = models.URLField(verify_exists=False,max_length=300)
    def _translate(self):
        return id_to_string(self.id)
    translate = property(_translate)
    def __unicode__(self):
        return "%s" % (self.url)

class ClickEntry(models.Model):
    action_time = models.DateTimeField('action time', auto_now=True)
    user_agent = models.CharField(max_length=200)
    remote_addr = models.CharField(max_length=200)
    remote_host = models.CharField(max_length=200)
    request_method = models.CharField(max_length=200)
    url = models.ForeignKey(ShortUrl)
    def load_meta(self, meta):
        self.user_agent = meta.get('HTTP_USER_AGENT',None)
        self.remote_addr = meta.get('REMOTE_ADDR',None)
        self.remote_host = meta.get('REMOTE_HOST', None)
        self.request_method = meta.get('REQUEST_METHOD', None)
    def __unicode__(self):
        return "%s" %(self.action_time)
    
