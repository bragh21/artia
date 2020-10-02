from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404

from .models import Projeto
from app_atividade.models import Atividade


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
