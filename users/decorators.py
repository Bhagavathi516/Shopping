from django.core.exceptions import PermissionDenied

def superuser_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        print(request.user.is_superuser)
        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view