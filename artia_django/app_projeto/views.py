from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse

from .models import Projeto
from app_atividade.models import Atividade

from .forms import ProjetoForm


class ProjetoView(TemplateView):
    template_name = 'appprojeto/projeto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projeto = Projeto.objects.filter(id=kwargs['pk'], nome=kwargs['nome'], ativo=True)
        if projeto:
            projeto = projeto[0]
            atividades = Atividade.objects.filter(projeto=projeto)
            context['title'] = f'{projeto} | ARTIA'
            context['projeto'] = projeto
            context['atividades'] = atividades
            context['perc'] = check_percentage(atividades)
            context['atrasado'] = check_atraso(atividades, projeto)
        else:
            raise Http404

        return context

class ProjetoAddView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Adicionar Projeto | ARTIA',
            'form': ProjetoForm()
        }
        return render(request, 'appprojeto/projeto_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ProjetoForm(request.POST)
        if form.is_valid():
            try:
                projeto = Projeto.objects.create(
                    nome=form.cleaned_data['nome'],
                    data_inicio=form.cleaned_data['data_inicio'],
                    data_fim=form.cleaned_data['data_fim']
                )
            except:
                return HttpResponseBadRequest("Something wrong with your inputs!")

            return redirect(reverse('appprojeto:projeto', kwargs={'nome': projeto.nome, 'pk': projeto.id}))
        return HttpResponseBadRequest("Something wrong with your inputs!")


def check_percentage(atividades):
    atividades_concluidas = 0
    n = 0
    for a in atividades:
        if a.finalizada is True:
            atividades_concluidas += 1

        n += 1

    if atividades_concluidas > 0:
        percentage = (atividades_concluidas / n) * 100
    else:
        percentage = 0

    return int(percentage)

def check_atraso(atividades, projeto):
    atrasado = 'Não'
    for a in atividades:
        if a.data_fim > projeto.data_fim and a.finalizada is False:
            atrasado = 'Sim'

    return atrasado        
