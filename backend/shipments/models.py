from django.db import models

from catalog.models import Item


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='Country name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class City(models.Model):
    name = models.CharField(max_length=50, help_text='City name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='cities',
                                help_text='Country where the city is located')

    def __str__(self):
        return f'{self.name}, {self.country}'

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name', 'country'],
                                    name='unique_city')
        ]


class Shipment(models.Model):
    class ShipmentStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        IN_TRANSIT = 'IN_TRANSIT', 'In transit'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELLED = 'CANCELLED', 'Cancelled'

    items = models.ManyToManyField(Item, related_name='shipments',
                                   help_text='Items delivered in this shipment')
    status = models.CharField(max_length=10,
                              choices=ShipmentStatus.choices,
                              default=ShipmentStatus.PENDING,
                              help_text='Shipment status')
    city = models.ForeignKey(City, on_delete=models.PROTECT,
                             related_name='shipments',
                             help_text='Destination city')
    address = models.CharField(max_length=150, help_text='Destination address')
    comment = models.CharField(max_length=300, null=True, blank=True,
                               help_text='Additional information')
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='Shipment creation date')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='Shipment last update date')
    sent_at = models.DateTimeField(null=True, blank=True,
                                   help_text='Shipment sent date')

    def __str__(self):
        return f'#{self.id} - {self.status}, {self.get_full_address()}'

    def get_full_address(self):
        return f'{self.address}, {self.city}'

    class Meta:
        ordering = ['-created_at']
