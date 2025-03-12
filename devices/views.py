from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Device, Lease

def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone_number, password=password)
        if user:
            login(request, user)
            return redirect('device_list')
        return HttpResponse("Invalid credentials", status=401)
    return render(request, 'devices/login.html')

def custom_logout_view(request):
    logout(request)
    return redirect('login')

class DeviceListView(View):
    def get(self, request):
        devices = Device.objects.filter(status='AVAILABLE')
        return render(request, 'devices/device_list.html', {'devices': devices})

class DeviceDetailView(View):
    def get(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        return render(request, 'devices/device_detail.html', {'device': device})

@method_decorator(login_required, name='dispatch')
class DeviceLeaseView(View):
    def post(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        
        if device.status != 'AVAILABLE':
            return HttpResponse("This device is not available for lease.", status=400)

        device.lease_device(request.user)
        return redirect('device_detail', device_id=device.id)

@method_decorator(login_required, name='dispatch')
class LeaseListView(View):
    def get(self, request):
        leases = Lease.objects.filter(user=request.user, returned_at__isnull=True)
        return render(request, 'devices/leased_devices.html', {'leases': leases})

@method_decorator(login_required, name='dispatch')
class DeviceReturnView(View):
    def post(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        
        if device.status != 'LEASED':
            return HttpResponse("This device is not currently leased.", status=400)
        
        device.return_device()
        return redirect('device_detail', device_id=device.id)
