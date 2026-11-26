import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Wait for the database to become available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB...")

        while True:
            try:
                connection.ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Still waiting for DB...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Connected!"))