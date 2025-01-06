from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import redirect_to_login


class CustomLoginView(LoginView):
    template_name = "public/login.html"
    success_url = "/"
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    template_name = "public/login.html"

    def render_to_response(self, context, **response_kwargs):
        return redirect_to_login(self.request.get_full_path(), settings.LOGIN_URL)
