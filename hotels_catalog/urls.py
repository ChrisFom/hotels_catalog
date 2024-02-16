
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/', include('hotels.api.urls'))
]
