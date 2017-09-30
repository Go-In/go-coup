from django import forms

class NameForm(forms.Form):
    coupon_name = forms.CharField(label='Coupon name', max_length=127)