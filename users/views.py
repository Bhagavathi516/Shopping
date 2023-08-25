from django.shortcuts import render, redirect
from .forms import UserSignupEmailForm, UserSignupProfileForm, UserSignupFormset, UserUpdationForm, UserLoginForm, ShoppingItemFormset
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import UserProfile
# from users.forms import ShoppingItemFormset
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from users.decorators import superuser_required
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.
def user_signup_view(request):
    user_signup_email_form = UserSignupEmailForm(request.POST or None)
    # user_signup_formset = UserSignupFormset(request.POST or None, prefix='profile')
    if user_signup_email_form.is_valid():
        user_signup_email_form.save()
        # for profile_form in user_signup_formset:
        #     if profile_form.cleaned_data:
        #         name = profile_form.cleaned_data['name']
        #         phone_number = profile_form.cleaned_data['phone_number']
        #         place = profile_form.cleaned_data['place']
                # UserProfile.objects.create(user=user, name=name, phone_number=phone_number, place=place)
        # username = user_signup_email_form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created! You are now able to log in!')
        return redirect('login')
    return render(request, 'users/signup.html',{'user_signup_email_form': user_signup_email_form})


@login_required
def user_profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdationForm(request.POST, instance=request.user)
        profile_formset = UserSignupFormset(request.POST, request.FILES, prefix='profile')
        if u_form.is_valid() and profile_formset.is_valid():
            # Process and save profile details and update user details
            u_form.save()
            for profile_form in profile_formset:
                if profile_form.cleaned_data:
                    name = profile_form.cleaned_data['name']
                    phone_number = profile_form.cleaned_data['phone_number']
                    place = profile_form.cleaned_data['place']
                    image = profile_form.cleaned_data['image']
                    user_profile.name = name
                    user_profile.phone_number = phone_number
                    user_profile.place = place
                    user_profile.image = image
                    user_profile.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  # Redirect to the profile page after updating details
    else:
        u_form = UserUpdationForm(instance=request.user)
        initial_data = {
            'name': user_profile.name,
            'phone_number': user_profile.phone_number,
            'place': user_profile.place,
            'image':user_profile.image
        }
        profile_formset = UserSignupFormset(initial=[initial_data], prefix='profile')
    return render(request, 'users/profile.html', {'profile_formset': profile_formset, 'u_form':u_form})


def user_login_view(request):
    user_login_form = UserLoginForm(request.POST or None)
    if user_login_form.is_valid():
        username_or_email = user_login_form.cleaned_data['username_or_email']
        # email = user_login_form.cleaned_data['email']
        password = user_login_form.cleaned_data['password']

        # Authenticate user with either username or email
        user = None
        if '@' in username_or_email:  # If input looks like an email
            try:
                # user = authenticate(request, email=username_or_email, password=password)
                user = User.objects.get(email=username_or_email)

            except User.DoesNotExist:
                pass
        else:  # Otherwise, treat as a username
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('item_list')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid login credentials')
            # Redirect back to the login page with the form data pre-filled
            return redirect('login')  # Replace with your actual URL name

    return render(request, 'users/login.html', {'login_form': user_login_form})
# def user_login_view(request):
#     login_form = UserLoginForm(request, data=request.POST or None)
#     if login_form.is_valid():
#         user = login_form.get_user()
#         login(request, user)
#         return redirect('item_list')
#     return render(request, 'users/login.html', {'login_form': login_form})

# Already done this in shopping app using forms
# def shopping_item_view(request):
#     shopping_item_formset = ShoppingItemFormset(request.POST or None, prefix='shopping_items')
#     if shopping_item_formset.is_valid():
#         for form in shopping_item_formset:
#             if form.is_valid():
#                 form.save()

@superuser_required
def superuser_view(request):
    if request.user.is_superuser:
        # Redirect superusers to the admin page
        return redirect(reverse('admin:index'))
    else:
        return HttpResponse("This is a superuser-only view.")
    

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('profile')