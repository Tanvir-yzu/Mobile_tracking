from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tracking.models import LocationData
from devices.models import Device
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
@login_required
def live_map_view(request):
    location_list = []
    for device in request.user.device_set.all():
        loc = LocationData.objects.filter(device=device).order_by('-timestamp').first()
        if loc:
            location_list.append(loc)  # Append LocationData object

    context = {
        'latest_locations': location_list,  # 👈 This is now a LIST, not a dict
    }
    return render(request, 'tracking/live_map.html', context)

@login_required
def location_history_view(request, device_id):
    device = Device.objects.get(id=device_id, owner=request.user)
    locations = LocationData.objects.filter(device=device).order_by('-timestamp')
    return render(request, 'tracking/location_history.html', {'locations': locations, 'device': device})

@login_required
def add_location_data(request):
    # ✅ Use 'owner' instead of 'user' to match your Device model
    user_devices = Device.objects.filter(owner=request.user)  # Fixed field name

    if request.method == 'POST':
        device_id = request.POST.get('device')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        speed = request.POST.get('speed', None)
        accuracy = request.POST.get('accuracy', None)

        try:
            device = Device.objects.get(id=device_id, owner=request.user)
            LocationData.objects.create(
                device=device,
                latitude=float(latitude),
                longitude=float(longitude),
                speed=float(speed) if speed else None,
                accuracy=float(accuracy) if accuracy else None,
                is_online=True
            )
            messages.success(request, 'Location data added successfully!')
            return redirect('add_location_data')
        except Device.DoesNotExist:
            messages.error(request, 'Invalid device or you do not have permission.')
        except Exception as e:
            messages.error(request, f'Error adding location: {str(e)}')

    context = {
        'user_devices': user_devices,
    }
    return render(request, 'tracking/add_location_data.html', context)
