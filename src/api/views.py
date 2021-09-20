from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import RequestLog
from .serializers import RequestLogSerializer


def _get_client_ip(request: Request) -> str:
    x_forwarded_for = request.META.get('HTTP_REMOTE_ADDR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view(['GET', 'POST'])
def handle_request_view(request: Request):
    if request.method == 'GET':
        queryset = RequestLog.objects.all()
        data = RequestLogSerializer(queryset, read_only=True, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        ipaddress = _get_client_ip(request)
        item = RequestLog.objects.create(ipaddress=ipaddress)
        data = RequestLogSerializer(item, read_only=True, many=False).data
        return Response(data=data, status=status.HTTP_201_CREATED)
