from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Road trip / Vehicle
    path('road-trip/', views.road_trip, name='road_trip'),
    path('book-vehicle/', views.book_vehicle, name='book_vehicle'),
    path('confirm-booking/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),

    # Hotels
    path("hotels/", views.hotel_list, name="hotel_list"),
    path("hotels/<int:hotel_id>/book/", views.hotel_booking, name="hotel_booking"),
    path("confirm-hotel/<int:booking_id>/", views.confirm_hotel_booking, name="confirm_hotel_booking"),

    # Food
    path("food/", views.food_list, name="food_list"),
    path("food/<int:food_id>/order/", views.order_food, name="order_food"),
    path('confirm-food/<int:order_id>/', views.confirm_food_order, name='confirm_food_order'),

    # Packages
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),

    # Contact
    path('contact/', views.contact, name='contact'),
]
