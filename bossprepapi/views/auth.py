from django.http import JsonResponse
from bossprepapi.models.users import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def google_auth_check(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST request required.'}, status=400)
    try:
        data = json.loads(request.body)
        uid = data.get('uid')
        if uid is None:
            return JsonResponse({'error': 'uid required.'}, status=400)
        exists = User.objects.filter(uid=uid).exists()
        return JsonResponse({'profileExists': exists})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
