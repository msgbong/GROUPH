from django import forms

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

MARITAL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
]

STAFF_TYPE_CHOICES = [
    ('teaching', 'Teaching Staff'),
    ('non_teaching', 'Non-Teaching Staff'),
]

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    address = forms.CharField(widget=forms.Textarea)
    nationality = forms.CharField(max_length=100)
    staff_type = forms.ChoiceField(choices=STAFF_TYPE_CHOICES, widget=forms.RadioSelect)
    bank_account_number = forms.CharField(max_length=100)
    
    def clean_staff_type(self):
        staff_type = self.cleaned_data['staff_type']
        if staff_type == '':
            raise forms.ValidationError("Please select a staff type")
        return staff_type



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    marital_status = forms.ChoiceField(choices=[('--Select--', '--Select--'), ('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')])
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    address = forms.CharField(widget=forms.Textarea)
    nationality = forms.CharField(max_length=50)
    staff_type = forms.ChoiceField(choices=[('teaching', 'Teaching Staff'), ('non_teaching', 'Non-Teaching Staff')], widget=forms.RadioSelect)
    bank_account_number = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        staff_type = cleaned_data.get('staff_type')
        if staff_type == None:
            raise forms.ValidationError("Please select either 'Teaching Staff' or 'Non-Teaching Staff'")
        return cleaned_data

