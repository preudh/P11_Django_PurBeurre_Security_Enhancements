from django.urls import path
from app_users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_request, name = 'login'),
    path('register/', views.register_request, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('my_account/', views.my_account, name = 'my_account'),

    # reset password urls
    # page to enter email address
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'password_reset_form.html'), name = 'password_reset'),
    # page to inform user that email has been sent
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name = 'password_reset_done'),
    # page to enter new password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name = 'password_reset_complete'),
]


