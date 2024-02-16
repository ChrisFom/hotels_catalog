from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from accounts.api import views

router = DefaultRouter()
router.register(r'users', views.AuthViewSet, basename='users')


urlpatterns = [

]

urlpatterns += router.urls
