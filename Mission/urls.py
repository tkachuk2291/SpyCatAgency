from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Mission.views import MissionViewSet, TargetViewSet

router = DefaultRouter()
router.register("mission", MissionViewSet, basename="spy-cat-mission"),
router.register("target", TargetViewSet, basename="spy-cat-target"),

urlpatterns = [path("", include(router.urls))]

app_name = "mission"