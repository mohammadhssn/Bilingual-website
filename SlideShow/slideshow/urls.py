from django.urls import path
from . import views

app_name = 'slideshow'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('change_lang/', views.ChangeLanguage.as_view(), name='change_lang'),

]
