from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254, help_text='eg. youremail@anyemail.com', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class ProductSizeForm(forms.Form):

        SIZES = (
        		('X', 'No size selected'),
        		('4', 'Size 4'),
        		('6', 'Size 6'),
        		('8', 'Size 8'),
        		('10','Size 10'),
        		('12', 'Size 12'),
        		('14', 'Size 14'),
        		('16', 'Size 16'),
        )
        size = forms.ChoiceField(label="size", choices=SIZES, required=False)
