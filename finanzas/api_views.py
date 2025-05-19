from rest_framework import viewsets, permissions
from .models import RegistroFinanciero
from .serializers import RegistroFinancieroSerializer

class RegistroFinancieroViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroFinancieroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RegistroFinanciero.objects.filter(usuario=self.request.user).order_by('-fecha')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
