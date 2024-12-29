from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Device
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('device_list')
        else:
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
