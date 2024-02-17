from django import forms
from .models import Customer


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['First_Name', 'Last_Name', 'Phone_Number', 'Email', 'Password']
        include = ['C_Password', 'OTP']
        First_Name = forms.CharField(max_length=50)
        Last_Name = forms.CharField(required=False)
        Phone_Number = forms.IntegerField()
        Email = forms.EmailField(max_length=50)
        Password = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['Last_Name'].required = False

    C_Password = forms.CharField(max_length=50)
    Email_OTP = forms.IntegerField()
    Ph_OTP = forms.IntegerField()
    Email_OTP_Verified = forms.BooleanField()
    Ph_OTP_Verified = forms.BooleanField()

    def clean_First_Name(self):
        first_name = self.cleaned_data.get('First_Name')
        if not first_name.isalpha():
            raise forms.ValidationError("ENTER A VALID NAME")
        return first_name

    def clean_Last_Name(self):
        last_name = self.cleaned_data.get('Last_Name')
        if last_name:
            if not last_name.isalpha():
                raise forms.ValidationError("ENTER A VALID NAME")
            return last_name

    def clean_Phone_Number(self):
        phone = self.cleaned_data.get('Phone_Number')
        if phone.isnumeric() is True:
            qs = Customer.objects.filter(Phone_Number=phone)
            if qs.exists():
                raise forms.ValidationError("PHONE NUMBER ALREADY EXISTS")
            elif len(phone) != 10:
                raise forms.ValidationError("ENTER A VALID PHONE NUMBER (Number of digits must be 10))")
            return phone
        else:
            raise forms.ValidationError("ENTER A VALID PHONE NUMBER")

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        qs = Customer.objects.filter(Email=email)
        if qs.exists():
            raise forms.ValidationError("EMAIL ALREADY EXISTS")
        return email

    def clean_Password(self):
        password = self.cleaned_data.get('Password')
        if len(password) < 8:
            raise forms.ValidationError("PASSWORD MUST CONTAIN ATLEAST 8 CHARACTERS")
        return password

    def clean_C_Password(self):
        password = self.cleaned_data.get('Password')
        c_password = self.cleaned_data.get('C_Password')
        if password != c_password:
            raise forms.ValidationError("PASSWORD DOES NOT MATCH")
        return c_password

    def clean_Email_OTP(self):
        otp = self.cleaned_data.get('Email_OTP')
        if len(str(otp)) != 6:
            print(1)
            print(otp)
            print(len(str(otp)))
            raise forms.ValidationError("OTP IS NOT VALID!..")
        return otp

    def clean_Email_OTP_Verified(self):
        otp_ver = self.cleaned_data.get('Email_OTP_Verified')
        if otp_ver is False:
            print(0)
            raise forms.ValidationError("OTP IS NOT VERIFIED!")
        return otp_ver

    def clean_Ph_OTP(self):
        otp = self.cleaned_data.get('Ph_OTP')
        if len(str(otp)) != 6:
            print(1)
            print(otp)
            print(len(str(otp)))
            raise forms.ValidationError("OTP IS NOT VALID!..")
        return otp

    def clean_Ph_OTP_Verified(self):
        otp_ver = self.cleaned_data.get('Ph_OTP_Verified')
        if otp_ver is False:
            print(0)
            raise forms.ValidationError("OTP IS NOT VERIFIED!")
        return otp_ver


class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('Email', 'Password',)
        Email = forms.CharField(max_length=50)
        Password = forms.CharField(max_length=50)

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        qs = Customer.objects.filter(Email=email)
        if not qs.exists():
            raise forms.ValidationError("EMAIL DOES NOT EXISTS")
        return email

    def clean_Password(self):
        password = self.cleaned_data.get('Password')
        if len(password) < 8:
            raise forms.ValidationError("PASSWORD MUST CONTAIN ATLEAST 8 CHARACTERS")

        return password
