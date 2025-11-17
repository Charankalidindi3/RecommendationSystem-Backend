from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ItemViewSet,UserActivitySet

router = DefaultRouter()
router.register('products',ItemViewSet,basename="Item")
router.register('users',UserViewSet,basename="User")
router.register('activities', UserActivitySet,basename="activity")

urlpatterns = [
    path('',include(router.urls)),
]