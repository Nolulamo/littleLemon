from django.urls import path
from . import views
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
]