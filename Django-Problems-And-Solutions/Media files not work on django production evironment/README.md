Problems: 

How to serve media files on django production evironment?

In me settings.py file :-

```python
DEBUG = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
LOGIN_URL = '/login/'
MEDIA_URL = '/media/'
```
In my urls.py file:-
```python
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

Solution:
[Answer](https://stackoverflow.com/questions/39051206/how-to-serve-media-files-on-django-production-evironment)