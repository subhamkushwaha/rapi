from home.Empserializer import EmpSerializer
from home.models import Emp
from rest_framework import viewsets
class Empviewset(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer