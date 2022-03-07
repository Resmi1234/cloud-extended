import os.path

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from phonenumber_field.modelfields import PhoneNumberField

from extendedcloudapp.models import Login, Receiver, Owner, Upload


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class OwnerRegister(forms.ModelForm):
    class Meta:
        model = Owner
        fields=('Name', 'Contact_No', 'Email', 'Address')

    def clean_phone(self):
        Contact_No = self.cleaned_data.get("Contact_No")
        z = PhoneNumberField.parse(Contact_No, "IN")
        if not PhoneNumberField.is_valid_number(z):
            raise forms.validationError("Number not in SG format")
        return Contact_No

class ReceiverRegister(forms.ModelForm):
    class Meta:
        model = Receiver
        fields=('Name', 'Contact_No', 'Email', 'Address')

    def clean_phone(self):
        Contact_No = self.cleaned_data.get("Contact_No")
        z = PhoneNumberField.parse(Contact_No, "IN")
        if not PhoneNumberField.is_valid_number(z):
            raise forms.validationError("Number not in SG format")
        return Contact_No



class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = [
            'Title',
            'Description',
            'Files'
        ]


    def clean_file(self):
        Files = self.cleaned_data.get("Files", False)
        destination = settings.MEDIA_ROOT + '/media/'
        if os.path.isfile(destination + Files.name):
            raise forms.ValidationError(
                'A file with the name "' + Files.name + '" already exists. Please, rename your file and try again.')
        else:
            return Files