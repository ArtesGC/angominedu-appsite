from django.urls import path
from matricula import views

app_name = 'matricula'
urlpatterns = [
    path('', views.index, name='index')
]
