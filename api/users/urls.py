from rest_framework import routers

from api.users.views import AuthViewSet, UserViewSet

app_name = "users"

router = routers.DefaultRouter()

router.register(r"user", UserViewSet, basename="root")
router.register(r"auth", AuthViewSet, basename="root")

urlpatterns = []

urlpatterns += router.urls
