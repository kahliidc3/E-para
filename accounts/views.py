from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, AddressForm
from .models import Address

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to our community.')
            return redirect('core:home')
        else:
            # If form is not valid, add a message
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def profile(request):
    try:
        address = request.user.addresses.first()
    except Address.DoesNotExist:
        address = None

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            if request.FILES.get('avatar'):
                request.user.avatar = request.FILES['avatar']
                request.user.save()
                messages.success(request, 'Profile picture updated successfully.')
        elif 'update_address' in request.POST:
            address_form = AddressForm(request.POST, instance=address)
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.user = request.user
                address.save()
                messages.success(request, 'Address updated successfully.')
        return redirect('accounts:profile')

    address_form = AddressForm(instance=address)
    return render(request, 'account/profile.html', {
        'address_form': address_form,
    })
