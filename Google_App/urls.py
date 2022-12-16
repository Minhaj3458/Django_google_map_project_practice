from django.urls import path
from .import views
app_name = 'Google_App'
urlpatterns = [
   path('', views.index, name='index'),
   path('home/', views.home, name='home')

]