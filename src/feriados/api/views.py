import urllib.request
import json

from rest_framework import authentication, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feriados.api.serializers import PublicHolidaySerializer


class ListHolidays(ListAPIView):

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    serializer_class = PublicHolidaySerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        with urllib.request.urlopen('https://date.nager.at/api/v2/publicholidays/2023/CR') as response:
            data = response.read()
            json_data = json.loads(data.decode('utf-8'))

        serializer = PublicHolidaySerializer(data=json_data, many=True)
        if serializer.is_valid():
            data_serializer = serializer.data

        page = self.paginate_queryset(data_serializer)
        if page is not None:
            return self.get_paginated_response(page)

        return Response({'data': data_serializer})