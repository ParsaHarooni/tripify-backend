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
        
    def validate_empty_values(self, data):
        return super().validate_empty_values(data)