from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get("REMOTE_ADDR"))

        ip = request.META.get("REMOTE_ADDR")
        if '127.0.0.1' == ip:
            return HttpResponse("okok")
