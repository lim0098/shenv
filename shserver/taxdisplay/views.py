from django.shortcuts import render
from rest_framework import viewsets
from taxdisplay.serializers import ProcurementSerializer,SalesSerializer
from taxdisplay.models import ProcurementProject,SalesProject
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class ProcurementViewsSet(viewsets.ModelViewSet):
    # queryset = TaxEstimate.objects.all().filter(items=id)
    queryset = ProcurementProject.objects.all()
    serializer_class = ProcurementSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,DjangoFilterBackend,)
    search_fields =['date']
    filterset_fields = ['date']
    
class SalesViewsSet(viewsets.ModelViewSet):
    queryset = SalesProject.objects.all()
    serializer_class = SalesSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,DjangoFilterBackend,)
    search_fields =['date']
    filterset_fields = ['date']