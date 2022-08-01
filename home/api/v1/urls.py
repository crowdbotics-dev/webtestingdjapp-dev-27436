from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TyidhhdViewSet, VretyuViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("tyidhhd", TyidhhdViewSet)
router.register("vretyu", VretyuViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
