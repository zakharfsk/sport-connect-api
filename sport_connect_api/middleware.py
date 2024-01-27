from django.core.handlers.wsgi import WSGIRequest


class TokenMiddleware:
    async def __call__(self, scope, receive, send):
        query_string = scope.get("query_string", b"").decode("utf-8")
        query_parameters = {key: value for key, value in (
            param.split("=") for param in query_string.split("&"))}
        token = query_parameters.get("token", None)
        scope["token"] = token
        # Проводим аутентификацию пользователя на основе токена

        # Добавляем пользователя в scope для дальнейшего использования в consumers

        return await super().__call__(scope, receive, send)


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request: WSGIRequest, *args, **kwargs):
        authorization = request.META.get("HTTP_AUTHORIZATION")
        if authorization and not authorization.startswith("Bearer "):
            request.META["HTTP_AUTHORIZATION"] = "Bearer " + authorization
        response = self._get_response(request)
        return response


