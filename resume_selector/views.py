from django.views import View
from django.http import JsonResponse

class DemoView(View):
    def get(self, request):
        return JsonResponse({'content': 'hello'})
