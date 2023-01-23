from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({"test": 123})

    def create(self, request, *args, **kwargs):
        return Response({"Hello": request.data["nome"]})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=["get"], detail=True)
    def denunciar(self, request, pk=None):
        pass
