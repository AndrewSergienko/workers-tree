from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

POSITION_CHOISES = (
    ("1", "Директор"),
    ("2", "Зам. директора"),
    ("3", "Начальник відділу"),
    ("4", "Зам. начальника відділу"),
    ("5", "Старший менеджер"),
    ("6", "Менеджер"),
    ("7", "Офісний працівник"),
)


class Worker(MPTTModel):
    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
    )
    full_name = models.CharField(max_length=150)
    position = models.CharField(choices=POSITION_CHOISES, max_length=1)
    date_of_employment = models.DateField(auto_now_add=True)
    email = models.EmailField()
