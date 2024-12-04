#users.serializers.py
from rest_framework import serializers
from taxdisplay.models import ProcurementProject,SalesProject


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
