from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseBadRequest, Http404
from django.urls import reverse

from .models import Atividade
from .forms import AtividadeForm
from app_projeto.models import Projeto

class AtividadeAddView(View):
    def get(self, request, *args, **kwargs):
        projeto = Projeto.objects.filter(id=kwargs['pk'])
        if projeto:
            context = {
                'title': 'Adicionar Atividade | ARTIA',
                'form': AtividadeForm(),
            }
            return render(request, 'appatividade/atividade_form.html', context)
        raise Http404

    def post(self, request, *args, **kwargs):
        projeto = Projeto.objects.filter(id=kwargs['pk'])
        if projeto:
            projeto = projeto[0]
            form = AtividadeForm(request.POST)
            if form.is_valid():
                try:
                    atividade = Atividade.objects.create(
                        nome=form.cleaned_data['nome'],
                        data_inicio=form.cleaned_data['data_inicio'],
                        data_fim=form.cleaned_data['data_fim'],
                        finalizada=form.cleaned_data['finalizada'],
                        projeto=projeto
                    )
                except Exception as e:
                    return HttpResponseBadRequest("Something wrong with your inputs!")
                
                return redirect(reverse('appprojeto:projeto', kwargs={'nome': projeto.nome, 'pk': projeto.id}))
            else:
                return HttpResponseBadRequest("Something wrong with your inputs!")
        raise Http404
