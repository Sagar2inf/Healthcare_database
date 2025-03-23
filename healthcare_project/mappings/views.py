from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingDetailSerializer
from patients.models import Patient
from doctors.models import Doctor

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator
        return obj.created_by == request.user

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PatientDoctorMappingDetailSerializer
        return PatientDoctorMappingSerializer
    
    def perform_create(self, serializer):
        # Check if patient belongs to the user
        patient_id = self.request.data.get('patient')
        try:
            patient = Patient.objects.get(id=patient_id, created_by=self.request.user)
        except Patient.DoesNotExist:
            raise permissions.exceptions.PermissionDenied(
                detail="You can only assign doctors to your own patients"
            )
        
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def patient_doctors(self, request, patient_id=None):
        try:
            # Verify patient belongs to user
            patient = Patient.objects.get(id=patient_id, created_by=request.user)
            mappings = PatientDoctorMapping.objects.filter(patient=patient)
            serializer = PatientDoctorMappingDetailSerializer(mappings, many=True)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response(
                {"detail": "Patient not found or you don't have permission"}, 
                status=status.HTTP_404_NOT_FOUND
            )