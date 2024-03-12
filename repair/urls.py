from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('servicemanage/', views.servicemanage, name='dashboard-servicemanage'),
    path('servicedelete/<int:pk>/',views.service_delete, name='dashboard-service-delete'),
    path('serviceupdate/<int:pk>/',views.service_update, name='dashboard-service-update'),
    path('serviceprovider/',views.serviceprovider, name='dashboard-serviceprovider'),
    # path('customerpage/',views.customerpage, name='dashboard-customer'),
    path('bookings/',views.booking, name='dashboard-booking'),
    path('booking/schedule/<int:pk>/',views.booking_schedule, name="dashboard-booking-schedule"),
    path('review/',views.review, name='dashboard-review'),
    path('booking/delete/<int:pk>/',views.booking_delete, name='dashboard-booking-delete'),
    path('reviewlist/',views.reviewlist, name='dashboard-reviewlist')
]