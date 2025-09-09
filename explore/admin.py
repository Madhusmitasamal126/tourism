from django.contrib import admin
from .models import Banner, TourPackage, PackageItem, VehicleBooking, Vehicle, Hotel, HotelBooking, Food, FoodOrder

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(PackageItem)
class PackageItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'package')


@admin.register(VehicleBooking)
class VehicleBookingAdmin(admin.ModelAdmin):
    list_display = ("name", "vehicle_type", "booking_date", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("vehicle_type", "booking_date")

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'badge', 'badge_color')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating', 'price')  # Added price
    search_fields = ('name', 'location')

@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'created_at')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ("name", "food", "quantity", "created_at")