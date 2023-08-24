from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of allowed URLs
        allowed_urls = [reverse('item_list'), reverse('login'), reverse('register')]
        
        if not request.user.is_authenticated and request.path not in allowed_urls:
            return HttpResponseForbidden("Access denied. You are not allowed to access this page.")
            # return redirect('login')  # Redirect to login page
        
        response = self.get_response(request)
        return response
