from django.urls import include, path

app_name = "api"

urlpatterns = [
    path(
        "users/",
        include(
            'api.users.urls',
        ),
    )
]
