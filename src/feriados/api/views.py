import datetime
import urllib.request
import json

from django.http import HttpResponse
from rest_framework import authentication, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from feriados.api.serializers import PublicHolidaySerializer


class ListHolidays(ListAPIView):

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        year = request.GET.get('year', '2024')
        country = request.GET.get('country', 'CR')
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date', '')
        name_filter = request.GET.get('localName', '')

        with urllib.request.urlopen('https://date.nager.at/api/v2/publicholidays/'+year+'/'+country) as response:
            data = response.read()
            json_data = json.loads(data.decode('utf-8'))

        serializer = PublicHolidaySerializer(data=json_data, many=True)
        if serializer.is_valid():
            data_serializer = serializer.data


        if not start_date:
            filtered_data = [
                holiday for holiday in data_serializer
                if (name_filter == '' or name_filter.lower() in holiday['localName'].lower())
            ]
            page = self.paginate_queryset(filtered_data)
            if page is not None:
                return self.get_paginated_response(page)

            return Response({'data': filtered_data})
        else:
            filtered_data = [
                holiday for holiday in data_serializer
                if start_date <= holiday['date'] <= end_date and (name_filter == '' or name_filter.lower() in holiday['localName'].lower())
            ]
            page = self.paginate_queryset(filtered_data)
            if page is not None:
                return self.get_paginated_response(page)

            return Response({'data': filtered_data})

