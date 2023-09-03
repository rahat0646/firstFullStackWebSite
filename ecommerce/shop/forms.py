from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm

class Login(forms.Form):
    number=forms.CharField(min_length=8,max_length=12,widget=forms.NumberInput(attrs={'id':'phone'}),error_messages={'required': 'Telefon belgiňizi giriziň'})
    # username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'id':'username'}))
    password=forms.CharField(widget = forms.PasswordInput(attrs={'id':'password'}))
    
class Register(UserCreationForm):
    phone=forms.CharField(max_length=8,widget=forms.NumberInput(attrs={'id':'phone'}))
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'id':'username'}))
    password1=forms.CharField(min_length=7,widget = forms.PasswordInput(attrs={'id':'password'}))
    password2=forms.CharField(min_length=7,widget = forms.PasswordInput(attrs={'id':'password'}))
    class Meta:
        model = User
        fields = ["phone","username","password1","password2"]

    def save(self,commit=True):
        user = super(Register,self).save(commit=False)
        user.username=self.cleaned_data['phone']
        user.email=self.cleaned_data['username']
        # user.is_staff=True
        if commit:
            user.save()
        return user
    
class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['name', 'last_name','adress']
        widgets ={
            'name':forms.TextInput(attrs={'class':'name info_field','placeholder': 'Adyňyz'}),
            'last_name':forms.TextInput(attrs={'class':'last_name info_field','placeholder': 'Familýaňz'}),
            'adress':forms.Textarea(attrs={'class':'info_field','placeholder': 'Salgyňyz'}),
        }
            
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StatusPayment(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_choices'] 
        widgets = {
            'payment_choices':forms.Select(attrs={'class':'name info_field'})
        }