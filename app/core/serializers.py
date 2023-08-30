from rest_framework import serializers
from core.models import Expense, Trip

class TripSerializer(serializers.Serializer):
    
    class Meta:
        model = Trip
        fields = '__all__'
        
        
class ExpenseSerializer(serializers.Serializer):
    
    class Meta:
        model = Expense
        fields = '__all__'