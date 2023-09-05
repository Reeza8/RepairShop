from django.utils.deprecation import MiddlewareMixin


# check if the user is authenticated
class TokenMiddleWare(MiddlewareMixin):
    def __call__(self, request):
        url = request.get_full_path()
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is None:
            if "token" not in url:
                raise Exception("you must authenticate.")
        return self.get_response(request)
