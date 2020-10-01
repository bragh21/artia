from django.urls import path

from .views import ProjetoView

app_name = 'appprojeto'
urlpatterns = [
    path('<str:nome>-<int:pk>/', ProjetoView.as_view(), name='projeto'),
]