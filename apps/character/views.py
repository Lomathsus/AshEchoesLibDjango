from rest_framework import viewsets

from .models import Character
from .serializer import CharacterSerializer
from ..common.abstract_models import BaseModelViewSet


class CharacterViewSet(BaseModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
