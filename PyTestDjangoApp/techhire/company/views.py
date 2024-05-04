from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Company
from .serializers import CompanySerializers


# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination