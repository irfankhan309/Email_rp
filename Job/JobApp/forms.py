from django import forms
from JobApp.models import Test_Form

#
# class ContactForm(forms.Form):
#     your_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)

class form_test(forms.ModelForm):
    class Meta:
        model = Test_Form
        fields = '__all__'
