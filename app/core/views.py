from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Trip
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status



class PingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Pong'}
        return Response(content, status=status.HTTP_200_OK)
    
    
class TripView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        try:
            trips = Trip.objects.get(owner=user)
        except ObjectDoesNotExist:
            trips = []
        res = {
                "trips": trips
            }
        return Response(res, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass
    
    def delete(self, request):
        pass