from django import forms

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')

class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_a,validate_for_len])
    sprincipal=forms.CharField(validators=[validate_for_a])
    sloc=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if e!=re:
            raise forms.ValidationError('Email not matched')
