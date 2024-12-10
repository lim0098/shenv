#users.serializers.py
from rest_framework import serializers
from taxdisplay.models import ProcurementProject,SalesProject,InputInvoice,OutputInvoice


class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProcurementProject
        fields='__all__'
        # fields=['id','username','email','mobile','avatar']
        
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesProject
        fields='__all__'
        # fields=['id','username','email','mobile','avatar']
        
class InputInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=InputInvoice
        fields='__all__'
        # fields=['id','username','email','mobile','avatar']
        
class OutputInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=OutputInvoice
        fields='__all__'
        # fields=['id','username','email','mobile','avatar']
