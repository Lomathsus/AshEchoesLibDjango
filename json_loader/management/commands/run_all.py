from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run all tasks"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting all tasks...")

        # 调用 load_json 管理命令
        call_command("load_json")
        self.stdout.write(self.style.SUCCESS("Completed load_json"))

        # 调用 process_data 管理命令
        call_command("process_data")
        self.stdout.write(self.style.SUCCESS("Completed process_data"))

        self.stdout.write(self.style.SUCCESS("All tasks completed"))
