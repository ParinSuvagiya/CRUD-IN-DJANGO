from django.forms import ModelForm,TextInput,PasswordInput
from .models import student

class rgstudent(ModelForm):
	class Meta:
		model=student
		fields=['name','email','password']
		widgets={ 'name':TextInput(attrs={'class':'form-control'}),
		'email':TextInput(attrs={'class':'form-control'}),
		'password':PasswordInput(attrs={'class':'form-control'}),
		}