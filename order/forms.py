from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Nairobi', 'Nairobi'),
		('Kiambu', 'Kiambu'),
		('Machakos', 'Machakos '),
		('Kajiado', 'Kajiado')
	)

	PAYMENT_METHOD_CHOICES = (
		('Mpesa', 'Mpesa | Till Number: 902939'),
		('TKash','Tkash | Buy Goods: 902978')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES, label="County")
	district =  forms.CharField(label="Location")
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']