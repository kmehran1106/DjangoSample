from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [
    path('requests', views.handle_request_view),
]