from django.urls import path
from .views import MappingListCreateView, PatientDoctorListView, MappingDeleteView

urlpatterns = [
    path('<int:patient_id>/', PatientDoctorListView.as_view(), name='patient-doctor-list'),
    path('<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
]