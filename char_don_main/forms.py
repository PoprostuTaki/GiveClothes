from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=32, help_text='Wymagane, powtórz hasło',
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Potwierdź Hasło'}))
    email = forms.EmailField(max_length=64, help_text='Wymagane, wprowadź poprawny adres e-mail', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    username = forms.CharField(max_length=24, help_text='Wymagane, wprowadź poprawną nazwę użytkownika',
                               widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    first_name = forms.CharField(max_length=24, help_text='Wymagane, wprowadź poprawne imię',
                                 widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=24, help_text='Wymagane, wprowadź poprawne nazwisko',
                                widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    password = forms.CharField(max_length=32, help_text='Wymagane, wprowadź poprawne hasło',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Hasła się różnią',)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user