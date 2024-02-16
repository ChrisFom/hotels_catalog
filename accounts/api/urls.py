from rest_framework.routers import DefaultRouter
from accounts.api import views

router = DefaultRouter()
router.register(r'users', views.AuthViewSet, basename='users')


urlpatterns = [

]

urlpatterns += router.urls
