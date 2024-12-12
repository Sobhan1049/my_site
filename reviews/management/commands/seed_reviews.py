import random
from django.core.management.base import BaseCommand
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models
from django_seed import Seed


class Command(BaseCommand):

    help = "This command creates Reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(review_models.Review, number, {
            "accuarcy" : lambda x : random.randint(0, 6),
            "communication" : lambda x : random.randint(0, 6),
            "cleanliness": lambda x: random.randint(0, 6),
            "check_in" : lambda x : random.randint(0, 6),
            "location": lambda x: random.randint(0, 6),
            "value": lambda x: random.randint(0, 6),
            "room" : lambda x: random.choice(rooms),
            "user" : lambda x: random.choice(users),

        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))