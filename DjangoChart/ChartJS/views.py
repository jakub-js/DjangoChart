from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pyodbc
import pandas as pd
import json

from .models import Chart
from rest_framework import viewsets
from .serializer import ChartSerializer


# Create your views here.
class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer


def home(response):
    return render(response, 'ChartJS/base.html', {})


def index(response):
    return render(response, 'ChartJS/home.html', {})


def get_data(request):
    server = 'vwpnwrsiwhsql.prodwr.vwpn.emea.vwg'
    database = 'IWH'
    username = 'M1_Qlik'
    password = 'M1_Qlik'
    connection = pyodbc.connect(
        'DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=false;UID=' + username + ';PWD=' + password)

    request = pd.read_sql("""   SELECT TOP 10 data, hour_number, ist
                                FROM IWH.dbo.M1_Counters_History
                                WHERE shift_number <>0 and hour_number<>0  and linia='FA7';""", connection)
    data = request.to_json()


    # data = {
    #     'sales': 100,
    #     'customers': 10,
    # }
    return JsonResponse(data, safe=False)
