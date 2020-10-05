from django.urls import path

from .views import ProjetoView, ProjetoAddView

app_name = 'appprojeto'
urlpatterns = [
    path('<str:nome>-<int:pk>/', ProjetoView.as_view(), name='projeto'),
    path('add/', ProjetoAddView.as_view(), name='projeto_add'),
]