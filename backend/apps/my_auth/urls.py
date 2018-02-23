from django.urls import path
from .views import SignUpView, SignUpDone

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name="sign_up"),
    path('sign-up-done/', SignUpDone.as_view(), name="sign_up_done"),
]
