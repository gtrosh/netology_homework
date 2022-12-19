from django.urls import path
from calculator.views import ingredients

urlpatterns = [
    path("<str:dish>/", ingredients, name="ingredients"),
]
