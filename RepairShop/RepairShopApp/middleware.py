from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

# check if the user is authenticated
class TokenMiddleWare(MiddlewareMixin):
    def __call__(self, request):
        url = request.get_full_path()
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is None:
            if "token" not in url and "admin" not in url:
                return JsonResponse({'You must authenticate first'}, status=401)
        return self.get_response(request)

