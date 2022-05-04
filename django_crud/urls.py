from django.urls import path

from health_check.views import ping


urlpatterns = [
    # 127.0.0.1:8000/ping
    path("ping", ping)
]
