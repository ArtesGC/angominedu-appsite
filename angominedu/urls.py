from django.urls import path
from angominedu import views

app_name = 'angominedu'
urlpatterns = [
    path('', views.index, name='index')
]
