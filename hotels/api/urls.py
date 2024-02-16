from django.urls import path
from hotels.api import views


urlpatterns = [
    path('hotels/',
         views.HotelListView.as_view(),
         name='hotels'),
]
