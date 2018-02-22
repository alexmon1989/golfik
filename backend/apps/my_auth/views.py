from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login


class MyLoginView(LoginView):
    """Класс для управления авторизацией пользователей."""

    def form_valid(self, form):
        """Авторизирует пользователя и возвращает код 200, если логин и пароль верны."""
        login(self.request, form.get_user())

        # Если пользователь не нажал "Запомнить меня", то сессия заканчивается при закрытии браузера.
        if not int(self.request.POST['rememberme']):
            self.request.session.set_expiry(0)
        return HttpResponse(status=200)

    def form_invalid(self, form):
        """Возвращает код 400, если введены неверные логин, пароль."""
        return HttpResponse(status=400)
