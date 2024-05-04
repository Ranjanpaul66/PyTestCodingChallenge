from rest_framework import routers

from .views import CompanyViewSet

company_router = routers.DefaultRouter()
company_router.register('companies', viewset=CompanyViewSet, basename='companies')
