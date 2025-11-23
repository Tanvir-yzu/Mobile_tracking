from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracking.models import LocationData
from devices.models import Device
from .models import LocationData
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

@require_POST
def add_location_data(request):
    try:
        # Parse incoming JSON data
        data = json.loads(request.body)
        
        # Extract required fields
        device_id = data.get('device_id')
        latitude = float(data.get('latitude'))
        longitude = float(data.get('longitude'))
        
        # Optional fields
        speed = data.get('speed')
        accuracy = data.get('accuracy')
        is_online = data.get('is_online', True)

        # Validate the device exists
        device = Device.objects.get(device_id=device_id)
        
        # Create and save the LocationData entry
        LocationData.objects.create(
            device=device,
            latitude=latitude,
            longitude=longitude,
            speed=float(speed) if speed else None,
            accuracy=float(accuracy) if accuracy else None,
            is_online=is_online
        )
        
        return JsonResponse({'status': 'success', 'message': 'Location saved'})
        
    except Device.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Device not found'}, status=404)
    except (json.JSONDecodeError, ValueError, KeyError) as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
