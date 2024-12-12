from django.core.management.base import BaseCommand
from rooms.models import Facility
from django_seed import Seed

class Command(BaseCommand):

    help = "This command creates Facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        Facilities = [
            "Private entrance",
            "paid parking on premises",
            "paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in Facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(Facilities)} Facilities created!"))
