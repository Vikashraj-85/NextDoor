from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create Password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )
    
    # forms.py
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone', 'city', 'profile_image']

        widgets = {

            'phone': forms.TextInput(attrs={
                'class': 'rk-form-input',
                'placeholder': 'Enter phone number'
            }),

            'city': forms.TextInput(attrs={
                'class': 'rk-form-input',
                'placeholder': 'Enter city'
            }),

            'profile_image': forms.FileInput(attrs={
                'class': 'rk-form-file'
            }),
        }
        
        # =====================================hots_room=======================
        from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property

        fields = [
            'title',
            'description',
            'price',
            'location',
            'room_type',
            'furnished',
            'available',
            'image'
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'rk-room-input',
                'placeholder': 'Enter room title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'rk-room-input',
                'placeholder': 'Enter room description',
                'rows': 4
            }),

            'price': forms.NumberInput(attrs={
                'class': 'rk-room-input',
                'placeholder': 'Enter room price'
            }),

            'location': forms.TextInput(attrs={
                'class': 'rk-room-input',
                'placeholder': 'Enter location'
            }),

            'room_type': forms.Select(attrs={
                'class': 'rk-room-input'
            }),

            'furnished': forms.CheckboxInput(attrs={
                'class': 'rk-check-input'
            }),

            'available': forms.CheckboxInput(attrs={
                'class': 'rk-check-input'
            }),

            'image': forms.FileInput(attrs={
                'class': 'rk-room-input'
            }),
        }