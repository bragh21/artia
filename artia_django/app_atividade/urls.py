from django.urls import path

from .views import AtividadeAddView

app_name = 'appatividade'
urlpatterns = [
    path('add/<int:pk>', AtividadeAddView.as_view(), name='atividade_add'),
]