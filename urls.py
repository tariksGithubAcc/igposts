from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('process-form/', process_form, name='process_form'),
    path('scrap-url/', scrap_view, name='scrap_url'),
]
