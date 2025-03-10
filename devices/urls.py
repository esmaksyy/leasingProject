from django.urls import path
from .views import DeviceListView, DeviceDetailView, DeviceLeaseView, login_view, custom_logout_view, LeaseListView
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', login_view, name='login'),
    path('devices/', DeviceListView.as_view(), name='device_list'),
    path('devices/<int:device_id>/', DeviceDetailView.as_view(), name='device_detail'),
    path('logout/', custom_logout_view, name='logout'),
    path('devices/<int:device_id>/lease/', DeviceLeaseView.as_view(), name='device_lease'),
    path('leases/', LeaseListView.as_view(), name='leased_devices'),

]
