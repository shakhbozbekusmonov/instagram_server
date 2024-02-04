from django.urls import path
from .views import SignUpAPIView, VerifyAPIView, GetVerificationAPIView, ChangeUserInfoAPIView, ChangeUserPhotoAPIView, \
    LoginAPIView, LoginRefreshAPIView, LogOutAPIView, ForgotPasswordAPIView, ResetPasswordAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshAPIView.as_view(), name='login_refresh'),
    path('logout/', LogOutAPIView.as_view(), name='logout'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('new-verify/', GetVerificationAPIView.as_view(), name='new-verify'),
    path('change-user/', ChangeUserInfoAPIView.as_view(), name='change-user'),
    path('change-user-photo/', ChangeUserPhotoAPIView.as_view(), name='change-user-photo'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
]
