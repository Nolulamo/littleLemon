from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated



class MenuItemsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

