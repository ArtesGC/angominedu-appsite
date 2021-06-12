from django.contrib.auth import login
from django.urls import path, include
from alunos import views

app_name = 'alunos'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('cadastrar/', views.cadastrar, name='cadastrar')
]
