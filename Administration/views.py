from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
# Create your views here.
@login_required
def Administration(request):
    pass
    return render (request, 'Administration/Dashboard.html')

# core/views.py


@csrf_exempt
@login_required
def save_sidebar_setting(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        expanded = data.get('expanded', True)
        setting = UserSettings.objects.get_or_create(user=request.user)[0]
        setting.sidebar_expanded = expanded
        setting.save()
        return JsonResponse({'status': 'saved'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
