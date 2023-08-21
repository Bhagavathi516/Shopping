from django.shortcuts import render, redirect
from .forms import UserSignupEmailForm, UserSignupProfileForm, UserSignupFormset, UserLoginForm, ShoppingItemFormset
# from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile
# from users.forms import ShoppingItemFormset
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_signup_view(request):
    user_signup_email_form = UserSignupEmailForm(request.POST or None)
    user_signup_formset = UserSignupFormset(request.POST or None, prefix='profile')
    if user_signup_email_form.is_valid() and user_signup_formset.is_valid():
        user = user_signup_email_form.save()
        for profile_form in user_signup_formset:
            if profile_form.cleaned_data:
                name = profile_form.cleaned_data['name']
                phone_number = profile_form.cleaned_data['phone_number']
                place = profile_form.cleaned_data['place']
                UserProfile.objects.create(user=user, name=name, phone_number=phone_number, place=place)
        # username = user_signup_email_form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created! You are now able to log in!')
        return redirect('login')
    return render(request, 'users/signup.html', {'user_signup_email_form':user_signup_email_form, 'user_signup_formset':user_signup_formset})

@login_required
def user_profile_view(request):
    # user_signup_formset = UserSignupFormset(request.POST or None, prefix='profile')
    # if user_signup_formset.is_valid():
    #     for profile_form in user_signup_formset:
    #         if profile_form.cleaned_data:
    #             name = profile_form.cleaned_data['name']
    #             phone_number = profile_form.cleaned_data['phone_number']
    #             place = profile_form.cleaned_data['place']
    #             UserProfile.objects.create(user=user, name=name, phone_number=phone_number, place=place)
    return render(request, 'users/profile.html')

def user_login_view(request):
    user_login_form = UserLoginForm(request.POST or None)
    if user_login_form.is_valid():
        username = user_login_form.cleaned_data['username']
        email = user_login_form.cleaned_data['email']
        password = user_login_form.cleaned_data['password']
        
        # Authenticate user with either username or email
        user = authenticate(request, username=username, email=email, password=password)
        #This is not working, I'm using in in-built login 
        if user is not None:
            login(request, user)
            return redirect('item_list')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid login credentials')
            # Redirect back to the login page with the form data pre-filled
            return redirect('login')  # Replace with your actual URL name
    
    return render(request, 'users/login.html', {'form': user_login_form})
# def user_login_view(request):
#     login_form = UserLoginForm(request.POST or None)
#     if login_form.is_valid():
#         user = login_form.get_user()
#         login(request, user)
#         return redirect('item_list')
#     return render(request, 'users/login.html', {'login_form': login_form})

#Already done this in shopping app using forms
# def shopping_item_view(request):
#     shopping_item_formset = ShoppingItemFormset(request.POST or None, prefix='shopping_items')
#     if shopping_item_formset.is_valid():
#         for form in shopping_item_formset:
#             if form.is_valid():
#                 form.save()