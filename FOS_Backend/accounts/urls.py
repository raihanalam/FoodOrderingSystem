from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    # Add other URLs as needed
     
    path('signup', views.sign_up, name='sign_up'),
    path('signin',views.sign_in, name='sign_in'),
    path('signout',views.sign_out,name='sign_out'),
]
