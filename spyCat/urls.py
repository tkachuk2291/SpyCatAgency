from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spyCat.views import SpyCatViewSet

router = DefaultRouter()
router.register("spy-cat", SpyCatViewSet, basename="spy-cat-user"),

urlpatterns = [path("", include(router.urls))]

app_name = "spy_cat"