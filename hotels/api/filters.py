import django_filters
from hotels.models import Hotel


class HotelFilter(django_filters.FilterSet):
    city_id = django_filters.NumberFilter(field_name='city_id')
    from_id = django_filters.NumberFilter(field_name='id', lookup_expr='gt')
    limit = django_filters.NumberFilter(method='custom_limit_filter')

    class Meta:
        model = Hotel
        fields = ['city_id', 'from_id', 'limit']

    def custom_limit_filter(self, queryset, name, value):
        return queryset[:value] if value else queryset
