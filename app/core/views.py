from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.forms.models import model_to_dict

from core.models import Trip



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
        res = dict(
            trips=trips
        )
        return Response(res, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        city = data.get("city") or None
        country = data.get("country") or None
        user = request.user
        if city is not None and country is not None:
            trip = Trip.objects.create(country=country, city=city, owner=user)
            res = dict(
                trip=model_to_dict(trip)
            )
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = dict(
                message = "Please fill the form correctly"
            )
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        data = request.data
        trip_id = data.get("trip_id") or None
        if trip_id is not None:
            try:
                trip = Trip.objects.get(pk=trip_id, owner=request.user)
                trip.delete()
                res = dict(
                    message = f"Trip with ID [{trip_id}] deleted"
                )
                return Response(res, status=status.HTTP_200_OK)
            except:
                res = dict(
                    message = "Trip not found"
                )
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
        else:
            res = dict(
                    message = "trip_id not provided"
                )
            return Response(res, status=status.HTTP_400_BAD_REQUEST)