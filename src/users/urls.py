from django.urls import path
from .views import SignupView, UserSettingsView


app_name = 'users'

urlpatterns = [
     path('signup/', 
          SignupView.as_view(), 
          name='signup'),
    
     path('settings/', 
          UserSettingsView.as_view(), 
          name='settings'),
]
