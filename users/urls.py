from django.urls import path
from .views import SignUpAPIView, VerifyAPIView, GetVerificationAPIView, ChangeUserInfoAPIView


urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('new-verify/', GetVerificationAPIView.as_view(), name='new-verify'),
    path('change-user/', ChangeUserInfoAPIView.as_view(), name='change-user'),
]
