import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models
from django_seed import Seed

Name = "lists"
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
        seeder.add_entity(list_models.Lists, number, {

            "user" : lambda x: random.choice(users),

        },)
        created = seeder.execute()
        cleaned =  flatten(list(created.values()))
        for  pk in cleaned:
            list_model = list_models.Lists.objects.get(pk=pk)
            to_add = rooms[random.randint(0 , 5) : random.randint(6,30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {Name} created!"))