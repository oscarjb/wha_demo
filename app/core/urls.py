from django.urls import path
from .views import Register_user

app_name = "core"

urlpatterns = [
    path('register/', Register_user.as_view(), name='register'),
]