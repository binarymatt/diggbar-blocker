from django.shortcuts import render_to_response
import re
import logging
digg_re = re.compile(r'http://digg.com/\w{1,8}/?$')
class FckDiggMiddleware(object):
    def process_request(self, request):
        
        if request.META.has_key('HTTP_REFERER'):
            logging.info(request.META['HTTP_REFERER'])
            if digg_re.search(request.META['HTTP_REFERER']):
                return render_to_response('fck_digg.html')