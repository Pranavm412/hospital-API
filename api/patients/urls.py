from django.urls import path
from .views import PatientListCreateView,PatientDetailView

urlpatterns = [
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('', PatientListCreateView.as_view(), name='patient-list-create'),
]