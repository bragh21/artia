from django.shortcuts import render
from django.views.generic import TemplateView
from app_projeto.models import Projeto


class HomeView(TemplateView):
    template_name = "apphome/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home | ARTIA'
        context['projetos'] = Projeto.objects.filter(ativo=True)
        return context