from django import forms
from userprofile.models import UserExtend


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'customer',
        ]