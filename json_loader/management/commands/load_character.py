import os
import json
import re

from dateutil import parser as dateutil
from django.core.management.base import BaseCommand
from apps.character.models import Character  # 确保导入实际的模型


class Command(BaseCommand):
    help = "Load JSON files into the database"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {filename}"))
