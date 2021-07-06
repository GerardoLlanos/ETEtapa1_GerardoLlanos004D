from django.urls import path
from .views import home, Ver, form_colaborador, form_mod_colaborador, form_del_colaborador
urlpatterns = [
    path('', home, name="home"),
    path('ver', Ver, name="ver"),
    path('form_colaborador', form_colaborador, name="form_colaborador"),
    path('form_mod_colaborador/<id>', form_mod_colaborador, name="form_mod_colaborador"),
    path('form_del_colaborador/<id>', form_del_colaborador, name="form_del_colaborador"),
]