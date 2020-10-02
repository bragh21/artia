from django.shortcuts import render
from django.views.generic import TemplateView
from app_projeto.models import Projeto
from app_atividade.models import Atividade
from app_projeto.views import check_percentage, check_atraso


class HomeView(TemplateView):
    template_name = "apphome/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projetos = Projeto.objects.filter(ativo=True)
        projetos_list = []
        for p in projetos:
            atividades = Atividade.objects.filter(projeto=p)
            projetos_list.append({
                'projeto' : p,
                'perc': check_percentage(atividades),
                'atrasado': check_atraso(atividades, p)
            })

        context['title'] = 'Home | ARTIA'
        context['projetos'] = projetos_list
        return context
