from django.urls import path

from .views import MeasurementCreateView, SensorCreateListView, SensorRetrieveUpdateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateListView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
