from django.http import JsonResponse
from .models import AuthToken


class TokenAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Allow normal browser pages for now
        if not request.path.startswith("/api/"):
            return self.get_response(request)

        token = request.headers.get("X-Auth-Token")

        if not token:
            return JsonResponse(
                {
                    "error": "X-Auth-Token header is required"
                },
                status=401
            )

        try:
            auth_token = AuthToken.objects.get(
                token=token,
                is_active=True
            )

        except AuthToken.DoesNotExist:
            return JsonResponse(
                {
                    "error": "Invalid or inactive token"
                },
                status=401
            )

        request.user_role = auth_token.role

        return self.get_response(request)