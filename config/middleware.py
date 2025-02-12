from django.core.handlers.wsgi import WSGIRequest


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request: WSGIRequest, *args, **kwargs):
        authorization = request.META.get("HTTP_AUTHORIZATION")
        if authorization and not authorization.startswith("Bearer "):
            request.META["HTTP_AUTHORIZATION"] = "Bearer " + authorization
        response = self._get_response(request)
        return response


