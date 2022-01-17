from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .form import PersonForm
from django.contrib.auth.decorators import login_required

# Documentação de making queries https://docs.djangoproject.com/en/4.0/topics/db/queries/

@login_required
def lista_clientes(request):
    persons = Person.objects.all()
    return render(request, 'pessoas.html', {'persons': persons})

@login_required
def novo_cliente(request):
    form = PersonForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'person_form.html', {'form': form})

@login_required
def atualizar_cliente(request, id):
    person = get_object_or_404(Person, pk=id)
    print(person)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'person_form.html', {'form': form})

@login_required
def deletar_cliente(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        person.delete()
        return redirect('lista_clientes')
    return render(request, 'person_delete_confirm.html', {'person': person})


# Create your views here.

