from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservation import views

router = DefaultRouter()

router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restuarant/menu/', include('reservation.urls')),
    path('restuarant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]