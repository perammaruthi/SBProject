from django.urls import path

from sb_app import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', views.UserViewSet)
router.register('payment', views.CreateTransactionViewSet)
router.register('user_profile', views.UserProfileViewSet)

urlpatterns = [
]
urlpatterns += router.urls