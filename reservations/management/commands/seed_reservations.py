import random
from datetime import datetime,timedelta
from django.core.management.base import BaseCommand
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models
from django_seed import Seed

Name = "reservations"
class Command(BaseCommand):

    help = f"This command creates {Name}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help=f"How many {Name} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(reservation_models.Reservation, number, {
            "status" : lambda x : random.choice(["panding", "confirmed", "canceled" ]),
            "guest" : lambda x: random.choice(users),
            "room": lambda x: random.choice(rooms),
            "check_in": lambda x: datetime.now(),
            "check_out": lambda x:datetime.now() + timedelta(days=random.randint(1, 30))

        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {Name} created!"))