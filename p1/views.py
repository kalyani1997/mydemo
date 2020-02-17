from django.shortcuts import render

# Create your views here.
# from p1.models import *
from p1.serializers import *
from rest_framework.viewsets import ModelViewSet

class DoctorOps(ModelViewSet):
    queryset = Doctor.activent.all()
    serializer_class = DoctorSerializer

class HospitalOps(ModelViewSet):
    queryset = Hospital.activent.all()
    serializer_class = HospitalSerializer

class PatientOps(ModelViewSet):
    queryset = Patient.activent.all()
    serializer_class = PatientSerializer

from rest_framework.viewsets import *
class My_viewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = Address.activent.all()
    serializer_class = AddressSerializer

class AddressOps(My_viewset):
    queryset = Address.activent.all()
    serializer_class = AddressSerializer


