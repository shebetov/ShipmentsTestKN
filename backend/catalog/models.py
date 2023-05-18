from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=50, help_text="Item name")
    weight = models.DecimalField(decimal_places=3, max_digits=6,
                                 validators=[
                                     MinValueValidator(Decimal('0.001'))],
                                 help_text="Item weight")
    is_fragile = models.BooleanField(default=False,
                                     help_text="Is item fragile?")
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text="Item creation date")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at", "name"]
