from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json

from feriados.api.serializers import PublicHolidaySerializer


# Create your views here.

def index(request):

    with urllib.request.urlopen('https://date.nager.at/api/v2/publicholidays/2023/CR') as response:
        data = response.read()

        json_data = json.loads(data.decode('utf-8'))

        serializer = PublicHolidaySerializer(data=json_data, many=True)

        if serializer.is_valid():
            data_serializer = serializer.data
            return render(request, 'feriados/index.html', {'data': data_serializer})
        else:
            return HttpResponse(serializer.errors, status=400)


