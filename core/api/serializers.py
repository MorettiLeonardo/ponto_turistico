from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico
from endereco.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ("id", "nome", "descricao", "aprovado",
                  "foto", "atracoes", "comentario", "avaliacoes", "endereco")
