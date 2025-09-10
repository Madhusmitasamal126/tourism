from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Banner, TourPackage, Vehicle, VehicleBooking, HotelBooking, Hotel, Food, FoodOrder, PackageItem
from .forms import VehicleBookingForm

# Homepage
def index(request):
    banners = Banner.objects.all()
    tour_packages = TourPackage.objects.all()
    return render(request, "index.html", {"banners": banners, "tour_packages": tour_packages})

# Tour package details
def package_detail(request, package_id):
    package = get_object_or_404(TourPackage, id=package_id)
    items = package.items.all()
    return render(request, "package_detail.html", {"package": package, "items": items})

# Item detail page
def item_detail(request, item_id):
    item = get_object_or_404(PackageItem, id=item_id)
    return render(request, "item_detail.html", {"item": item})

# Vehicles
def road_trip(request):
    vehicles = Vehicle.objects.all()
    return render(request, "road-trip.html", {"vehicles": vehicles})

def book_vehicle(request):
    vehicle_type = request.GET.get("type")
    if request.method == "POST":
        form = VehicleBookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            send_mail(
                subject="Your Vehicle Booking is Confirmed ✅",
                message=f"Hi {booking.name},\nYour {booking.vehicle_type} booking is confirmed.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.email],
                fail_silently=True
            )
            messages.success(request, "✅ Booking submitted successfully!")
            return redirect("confirm_booking", booking_id=booking.id)
    else:
        form = VehicleBookingForm(initial={"vehicle_type": vehicle_type} if vehicle_type else None)
    return render(request, "book_vehicle.html", {"form": form})

def confirm_booking(request, booking_id):
    booking = get_object_or_404(VehicleBooking, id=booking_id)
    return render(request, "confirm_booking.html", {"booking": booking})

# Hotels
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, "hotels.html", {"hotels": hotels})

def hotel_booking(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        if name and email:
            booking = hotel.bookings.create(name=name, email=email)
            send_mail(
                subject="Hotel Booking Confirmed ✅",
                message=f"Hi {booking.name},\nYour booking at {hotel.name} is confirmed.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.email],
                fail_silently=True
            )
            messages.success(request, f"✅ Booking for {hotel.name} confirmed!")
            return redirect("confirm_hotel_booking", booking_id=booking.id)
    return render(request, "hotel_booking.html", {"hotel": hotel})

def confirm_hotel_booking(request, booking_id):
    booking = get_object_or_404(HotelBooking, id=booking_id)
    return render(request, "confirm_booking.html", {"booking": booking})

# Food
def food_list(request):
    foods = Food.objects.all()
    return render(request, "food.html", {"foods": foods})

def order_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        quantity = int(request.POST.get("quantity", 1))
        if name and email:
            order = FoodOrder.objects.create(food=food, name=name, email=email, quantity=quantity)
            send_mail(
                subject="Your Food Order is Confirmed 🍲",
                message=f"Hi {order.name},\nYour order for {order.quantity} x {order.food.name} is confirmed.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[order.email],
                fail_silently=True
            )
            messages.success(request, f"✅ Your order for {food.name} has been placed!")
            return redirect("confirm_food_order", order_id=order.id)
    return render(request, "food_order.html", {"food": food})

def confirm_food_order(request, order_id):
    order = get_object_or_404(FoodOrder, id=order_id)
    return render(request, "confirm_booking.html", {"order": order})

# Contact
def contact(request):
    return render(request, "contact.html")
