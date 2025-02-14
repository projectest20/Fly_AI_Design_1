from .views import index , results_page
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('results.html', results_page, name='results'),
]