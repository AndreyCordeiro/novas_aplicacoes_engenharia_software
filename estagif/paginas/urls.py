from django.urls import path
from .views import SobreView, InicioView

urlpatterns = [
    path("", InicioView.as_view(), name="inicio"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]
