from django.urls import include, path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.enter_view, name='main-view'),
    url('password_reset/', auth_views.PasswordResetView.as_view(template_name="admin/registration/password_reset_form.html", html_email_template_name="admin/registration/password_reset_email.html"), name='password_reset'),
    url('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="admin/registration/password_reset_done.html"), name='password_reset_done'),
    url('password_change/', auth_views.PasswordChangeView.as_view(template_name="admin/registration/password_change_form.html"), name='password_change'),
    url('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name="admin/registration/password_change_done.html"), name='password_change_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name="admin/registration/password_reset_confirm.html"), name='password_reset_confirm'),
    url('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="admin/registration/password_reset_complete.html"), name='password_reset_complete'),

]