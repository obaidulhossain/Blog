from .models import *

def sidebar_setting(request):
    if request.user.is_authenticated:
        try:
            setting = UserSettings.objects.get(user=request.user)
            return {'sidebar_expanded': setting.sidebar_expanded}
        except UserSettings.DoesNotExist:
            return {'sidebar_expanded': True}
    return {'sidebar_expanded': True}
