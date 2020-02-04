from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
    def clean_name(self):
              name = self.cleaned_data['name']
              if len(name) <= 0:
                 raise forms.ValidationError(
                                'please fill in your name')
              return name

    def clean_email(self):
              email = self.cleaned_data['email']
              if len(email) <= 0:
                 raise forms.ValidationError(
                                'please fill in your emailaddress')
              return email

    def clean_phone(self):
              phone = self.cleaned_data['phone']
              if len(phone) <= 7:
                 raise forms.ValidationError(
                                'please fill in your phonenumber')
              return phone

    def clean_message(self):
              message = self.cleaned_data['message']
              if len(message) <= 10:
                 raise forms.ValidationError(
                                'please fill in a message')
              return message
