from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .api_permissions import OnlyAdminCanCreate

from products.models import Category, Product
from .serializers import (
    CategoryModelSerializer,
    ProductModelSerializer,
    OrderModelSerializer
)

# Create your views here.


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryListOnlyApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderApiView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, OnlyAdminCanCreate]

    def post(self, request, pk=None, format=None):
        serializer = OrderModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        if not pk:
            orders = Order.objects.all()
            serializer = OrderModelSerializer(orders, many=True)
        else:
            order = Order.objects.get(pk=pk)
            serializer = OrderModelSerializer(order)

        return Response(serializer.data)
