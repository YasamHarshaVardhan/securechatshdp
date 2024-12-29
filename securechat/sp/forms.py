from django import forms
from .models import U1, U2

# Form for U1 model
class U1Form(forms.ModelForm):
    class Meta:
        model = U1
        fields = ['msg1']  # Include the fields you want in the form

# Form for U2 model
class U2Form(forms.ModelForm):
    class Meta:
        model = U2
        fields = ['msg2']  # Include the fields you want in the form
