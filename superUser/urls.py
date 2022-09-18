from django.urls import path

from . import views
#from .views import Registration, registration
urlpatterns = [
    #path('register/', Registration.as_view(), name = 'register'),
    path('register/', views.registration , name= 'registration'),

]