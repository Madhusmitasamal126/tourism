# explore/models.py
from django.db import models

# Banner model for homepage slider
class Banner(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)  # optional link when clicked
    order = models.PositiveIntegerField(default=0)  # order in slider

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Banner {self.id}"


# Tour Package model
class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tour_packages/')
    description = models.TextField()
    url = models.URLField(blank=True, null=True)  # details page link

    def __str__(self):
        return self.title


# Items inside each Tour Package
class PackageItem(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='package_items/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.package.title})"

# from django.db import models

VEHICLE_CHOICES = [
    ('car', 'Sedan Car'),
    ('suv', 'SUV'),
    ('bike', 'Bike'),
    ('bus', 'Mini Bus'),
]

class VehicleBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200, blank=True, null=True)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type} ({self.booking_date})"

from django.db import models

BADGE_COLOR_CHOICES = [
    ('red', 'Red'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('purple', 'Purple'),
    ('blue', 'Blue'),
]

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='vehicles/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField(default=0)  # 0 to 5
    slug = models.SlugField(unique=True)
    badge = models.CharField(max_length=50, blank=True, null=True)
    badge_color = models.CharField(max_length=20, choices=BADGE_COLOR_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name


# from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    rating = models.IntegerField(default=3)  # 1 to 5
    image = models.ImageField(upload_to="hotels/")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Added price

    def __str__(self):
        return self.name


class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} booked {self.hotel.name}"
    

#    from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="food/")

    def __str__(self):
        return self.name


class FoodOrder(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.name} ordered {self.food.name} ({self.quantity})"
