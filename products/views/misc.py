from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from products.models import Order, Review, Category
from products.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from products.serializers import OrderSerializer, ReviewSerializer, CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer