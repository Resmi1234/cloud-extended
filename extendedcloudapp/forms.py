

from django import forms

from django.contrib.auth.forms import UserCreationForm


from phonenumber_field.modelfields import PhoneNumberField

from extendedcloudapp.models import Login, Receiver, Owner, Upload, Request, Download


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
            Files = self.cleaned_data.get('Files')
            for instance in Upload.objects.all():
                if instance.Files == Files:
                    raise forms.ValidationError('Upload with this Files already exists' + Files)
            return Files



class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('User','Name', 'Email', 'File_Name', 'Message', 'Status')


class DownloadForm(forms.ModelForm):

    class Meta:
        model = Download
        fields = ('dec_key',)