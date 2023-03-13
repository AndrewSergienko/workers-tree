import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from workers.models import POSITION_CHOISES, Worker


class Command(BaseCommand):
    help = "Creating Worker models"

    def handle(self, *args, **kwargs):
        position_num_ranges = (
            4,
            4,
            4,
            8,
            10,
            10,
        )
        self.stdout.write("Start creating...")
        seeder = Seed.seeder()
        parent_workers = [self.create_worker(seeder, "1")]

        for number, position in zip(position_num_ranges, POSITION_CHOISES[1:]):
            new_parent_workers = []
            for _ in range(len(parent_workers) * number):
                new_parent_workers.append(
                    self.create_worker(
                        seeder, position[0], random.choice(parent_workers)
                    )
                )
            parent_workers = new_parent_workers

    def create_worker(self, seeder, position, parent=None):
        return Worker.objects.create(
            full_name=seeder.faker.name(),
            email=seeder.faker.email(),
            date_of_employment=seeder.faker.date_object(),
            position=position[0],
            parent=parent,
        )
