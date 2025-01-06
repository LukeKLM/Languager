from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        except_url = (settings.LOGIN_URL, settings.ADMIN_URL)
        if not request.user.is_authenticated and not any(
            (request.path.startswith(url) for url in except_url),
        ):
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
