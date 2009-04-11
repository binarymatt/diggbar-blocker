======================
Django Diggbar Blocker
======================
The Diggbar blocker redirects any request coming from the diggbar to a custom template.

Installation
============

#. add the diggbar app to your python path

#. add the following middleware to your project's settings.py:

    ``'diggbar.middleware.FckDiggMiddleware',``
    
#. if you want the provided template(something i would not suggest), add the 
    diggbar to the INSTALLED_APPS in settings.py. Otherwise, create your own fck_digg.html