from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Mapping
from .serializers import MappingSerializer

class MappingListCreateView(ListCreateAPIView): 
    queryset = Mapping.objects.all() 
    serializer_class = MappingSerializer 
    permission_classes = [IsAuthenticated]

class PatientDoctorListView(ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Mapping.objects.filter(patient__id=patient_id)

class MappingDeleteView(DestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mapping.objects.filter(id=self.kwargs['id'])