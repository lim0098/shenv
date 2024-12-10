from django.shortcuts import render
from rest_framework import viewsets,generics
from taxdisplay.serializers import ProcurementSerializer,SalesSerializer,InputInvoiceSerializer,OutputInvoiceSerializer
# from taxdisplay.serializers import ProcurementSerializer,SalesSerializer,InputInvoiceSerializer,OutputInvoiceSerializer,InputInvoiceListSerializer,OutputInvoiceListSerializer
from taxdisplay.models import ProcurementProject,SalesProject,InputInvoice,OutputInvoice
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
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

from rest_framework import status
from rest_framework.response import Response

class InputInvoiceViewsSet(viewsets.ModelViewSet):
    queryset = InputInvoice.objects.all()
    serializer_class = InputInvoiceSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,DjangoFilterBackend,)
    search_fields =['date']
    filterset_fields = ['date']
    
    def create(self, request, *args, **kwargs):
        if isinstance(request.data,list):
            serializer = self.get_serializer(data=request.data,many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(methods=['delete'],detail=False)
    def multiple_delete(self,request,*args,**kwargs):
        ids=request.query_params.get('ids',None)
        if not ids:
            return Response(status=status.HTTP_404_NOT_FOUND)
        btn_ids=ids.split(',')
        btn_ids=[int(x) for x in btn_ids if x.split()]
        buttons = InputInvoice.objects.filter(id__in=btn_ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OutputInvoiceViewsSet(viewsets.ModelViewSet):
    queryset = OutputInvoice.objects.all()
    serializer_class = OutputInvoiceSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,DjangoFilterBackend,)
    search_fields =['date']
    filterset_fields = ['date']
    
    def create(self, request, *args, **kwargs):
        if isinstance(request.data,list):
            serializer = self.get_serializer(data=request.data,many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['delete'],detail=False)
    def multiple_delete(self,request,*args,**kwargs):
        ids=request.query_params.get('ids',None)
        if not ids:
            return Response(status=status.HTTP_404_NOT_FOUND)
        btn_ids=ids.split(',')
        btn_ids=[int(x) for x in btn_ids if x.split()]
        buttons = OutputInvoice.objects.filter(id__in=btn_ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        