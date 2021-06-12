from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def cadastrar(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('etudiorder:index')
    context = {'title': 'Etudi-Order | cadastro', 'form': form}
    return render(request, 'registration/cadastrar.html', context)
