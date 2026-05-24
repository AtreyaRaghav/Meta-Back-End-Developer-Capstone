from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Restaurant.serializers import UserSerializer, bookingSerializer, menuSerializer
from rest_framework.decorators import api_view
from Restaurant.models import Booking, Menu
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'Restaurant/index.html', {})



# class bookingView(APIView):

#     def get(self, request):
#         items = booking.objects.all()
#         serializer = bookingSerializer(items, many=True)
#         return Response(serializer.data)


# class menuView(APIView):
#     def post(self, request):
#         serializer = menuSerializer(data= request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success", "data":serializer.data})



# # Create your views here. 
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all() 
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = MenuItem.objects.all() 
#     serializer_class = MenuItemSerializer



class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer