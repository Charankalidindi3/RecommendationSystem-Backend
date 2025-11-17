from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ItemViewSet
router = DefaultRouter()
router.register('items',ItemViewSet,basename="Item")
router.register('users',UserViewSet,basename="User")

urlpatterns = [
    path('',include(router.urls)),
    # path('user/',ItemViewSet.as_view()),
    # path('item/',)
]