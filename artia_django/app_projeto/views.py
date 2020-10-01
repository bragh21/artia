from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404

from .models import Projeto


class ProjetoView(TemplateView):
    template_name = 'appprojeto/projeto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projeto = Projeto.objects.filter(id=kwargs['pk'], nome=kwargs['nome'], ativo=True)
        print(projeto)
        if projeto:
            print(projeto[0])
            projeto = projeto[0]
            context['title'] = f'{projeto} | ARTIA'
            context['projeto'] = projeto
        else:
            raise Http404

        return context 
