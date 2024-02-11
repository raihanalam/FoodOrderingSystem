from django.urls import path
from .views import landing_page

urlpatterns = [
    # Other URL patterns
    path('', landing_page, name='landing_page'),
]
