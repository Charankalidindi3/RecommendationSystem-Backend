from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Items.models import Items
from Users.models import User
from .serializers import ItemSerializer,UserSerializer

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    lookup_field = 'id'  # optional, defaults to pk

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):   # <-- THIS HANDLES GET /users/{id}/
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, id=None):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    


class ItemViewSet(viewsets.ViewSet):
    lookup_field = 'id'  # optional, defaults to pk

    def list(self, request):
        queryset = Items.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):   # <-- GET /items/{id}/
        item = get_object_or_404(Items, id=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, id=None):     # <-- PUT /items/{id}/
        item = get_object_or_404(Items, id=id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None):    # <-- DELETE /items/{id}/
        item = get_object_or_404(Items, id=id)
        item.delete()
        return Response({'message': 'Item deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)