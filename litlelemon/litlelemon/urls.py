from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservation import views

router = DefaultRouter()

router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/menu/', include('reservation.urls')),
    path('restaurant/booking/', include(router.urls)),
]