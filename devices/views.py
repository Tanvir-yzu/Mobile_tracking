from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Device
from .forms import DeviceForm
import uuid  # Add this import

@login_required
def add_device_view(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.owner = request.user
            # Generate unique device ID
            device.device_id = str(uuid.uuid4())[:10].upper()  # Short unique ID
            device.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'devices/add_device.html', {'form': form})  # Fixed template path

# Keep existing views
@login_required
def device_list_view(request):
    devices = request.user.device_set.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

@login_required
def device_settings_view(request, device_id):
    device = Device.objects.get(id=device_id, owner=request.user)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/device_settings.html', {'form': form})