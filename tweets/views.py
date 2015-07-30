from django.http import JsonResponse
from django.views.decorators.http import require_POST


@require_POST
def create(request):
    return JsonResponse({'status': 'OK'})


def test(request):
    return JsonResponse({'test': 'vasa'})