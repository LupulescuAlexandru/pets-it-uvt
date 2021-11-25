"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, re_path, path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from animal.views import AnimalAutoComplete, ProprietarAutoComplete
from my_admin.views import register

@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    url('register/', register, name='register'),
    path('', include('my_admin.urls')),
    re_path(r'^', admin.site.urls),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),
    url(
        'animal-autocomplete/',
        AnimalAutoComplete.as_view(

        ),
        name='animal-autocomplete',
    ),
    url(
        'proprietar-autocomplete/',
        ProprietarAutoComplete.as_view(

        ),
        name='proprietar-autocomplete',
    ),
]
