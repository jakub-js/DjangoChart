from django.shortcuts import render
from .models import Chart
from rest_framework import viewsets
from .serializer import ChartSerializer


# Create your views here.
class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
