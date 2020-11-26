from django.urls import path

from sb_app import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', views.CreateUserViewSet)
router.register('payment', views.CreateTransactionViewSet)

urlpatterns = [
    # path('register', views.CreateUserViewSet, name='register'),
    path('logout', views.LogoutUserAPIView, name='logout')
]
urlpatterns += router.urls