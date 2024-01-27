

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
