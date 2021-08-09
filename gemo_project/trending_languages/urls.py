from django.urls import path
from . views import list_top_100_language


urlpatterns = [
    path('top_100', list_top_100_language, name='list_top_100_language'),
]
