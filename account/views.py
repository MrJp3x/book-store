from django.http import JsonResponse
from django.shortcuts import render
from .models import User
from .forms import UserProfileForm
from django.views.generic import UpdateView, CreateView


class BaseProfile:
    model = User
    form_class = UserProfileForm
    template_name = None
    success_url = '/accounts/profile/'  # todo: maybe should change

    def __init__(self):
        self.request = None

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        role = form.cleaned_data['role']
        company_name = form.cleaned_data['company_name']
        company_address = form.cleaned_data['company_address']
        tax_number = form.cleaned_data['tax_number']

        if role == 'publisher' and (not company_name or not company_address or not tax_number):
            return JsonResponse(
                {'error': 'For Book Publishers, company_name, company_address, and tax_number are required.'},
                status=400)

        self.object = form.save()
        return JsonResponse({'success': self.success_message})

    def form_invalid(form):
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)


class ProfileView(BaseProfile, UpdateView):
    template_name = 'account/profile.html'
    success_message = 'Profile updated successfully.'


class CreateProfileView(BaseProfile, CreateView):
    template_name = 'account/create_profile.html'
    success_message = 'Profile created successfully.'
