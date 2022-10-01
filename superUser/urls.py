from django.urls import path

from . import views
#from .views import Registration, registration
urlpatterns = [
    #path('register/', Registration.as_view(), name = 'register'),
    path('registration/', views.registration , name= 'registration'),
    path('registration/login', views.log_in , name= 'log_in'),
]