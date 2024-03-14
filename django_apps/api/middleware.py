from django.utils.deprecation import MiddlewareMixin


class ApiMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass