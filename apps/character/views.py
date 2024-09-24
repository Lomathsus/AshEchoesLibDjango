from .models import Character
from .serializer import CharacterSerializer
from common.abstract_class import BaseModelViewSet


class CharacterViewSet(BaseModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
