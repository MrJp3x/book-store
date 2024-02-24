
from django import forms
from .models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'role': forms.Select(choices=User.USER_ROLE, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.cleaned_data = None
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget.attrs['disabled'] = True  # Disable role field in the form

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        company_name = cleaned_data.get('company_name')
        company_address = cleaned_data.get('company_address')
        tax_number = cleaned_data.get('tax_number')

        # Check if role is "Book Publisher" and required fields are not provided
        if role == 'publisher':
            if not company_name or not company_address or not tax_number:
                raise forms.ValidationError(
                    "For Book Publishers, company_name, company_address, and tax_number are required.")

        return cleaned_data

