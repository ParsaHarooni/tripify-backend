import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Sum, Avg
from core.models import Trip, Expense



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
            trips = Trip.objects.filter(owner=user)
        except ObjectDoesNotExist:
            trips = []
        res = dict(
            trips=json.loads(serializers.serialize('json', trips))
        )
        return Response(res, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        city = data.get("city") or None
        country = data.get("country") or None
        people = data.get("people") or None
        user = request.user
        if None not in [city, country, people]:
            predicted_price = Expense.objects.filter(trip__city=city).aggregate(Avg(Sum('price')))
            trip = Trip.objects.create(country=country, city=city, owner=user, people=people)
            res = dict(
                trip=model_to_dict(trip),
                predicted_price = predicted_price
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
                    message = "Trip not found",
                )
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
        else:
            res = dict(
                    message = "trip_id not provided"
                )
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class ExpenseView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        trip_id = request.data.get("trip_id") or None
        if trip_id is not None:
            try:
                trip = Trip.objects.get(pk=trip_id)
                expenses = Expense.objects.filter(trip__pk=trip_id) or None
                if expenses != None:
                    costs = expenses.aggregate(Sum('price'))
                    average_costs = costs.get("price__sum") / trip.people
                    res = dict(
                        expenses = json.loads(serializers.serialize('json', expenses)),
                        average_costs = average_costs
                    )
                    return Response(res, status=status.HTTP_200_OK)
                else:
                    res = dict(
                        expenses = [],
                        average_costs = 0
                    )
                    return Response(res, status=status.HTTP_200_OK)
            except Exception as e:
                res = dict(
                    message = "Trip not found",
                    e=str(e)
                )
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
        else:
            res = dict(
                    message = "trip_id not provided"
                )
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        trip_id = request.data.get("trip_id") or None
        reason = request.data.get("reason") or None
        price = request.data.get("price") or None
        category = request.data.get("category") or None
        if None not in [trip_id, reason, price, category]:
            try:
                trip = Trip.objects.get(pk=trip_id, owner=request.user)
                expense = Expense.objects.create(trip=trip, reason=reason, price=price, category=category)
                res = dict(
                        expenses = model_to_dict(expense)
                    )
                return Response(res, status=status.HTTP_200_OK)
            except:
                res = dict(
                        message = "Trip was not found"
                    )
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
        else:
            res = dict(
                message = "Please provide trip_id, reason, price, category"
            )
            return Response(res, status=status.HTTP_400_BAD_REQUEST)