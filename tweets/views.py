from django.http import JsonResponse
from django.views.decorators.http import require_POST

def add(request):
    print(request)
    return JsonResponse({'status': 'OK'})


def test(request):
    return JsonResponse({'test': 'vasa'})
