from django.urls import include, path

urlpatterns = [
    path("api/", include([
        path("shipments/", include("shipments.urls")),
    ])),
]
