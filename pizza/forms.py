from django import forms
from .models import Pizza,Size,UserProfileInfo


from django.contrib.auth.models import User
# class Pizzaform(forms.Form):
#     topping1=forms.CharField(label='Topping1',max_length=120,widget=forms.TextInput)
#     topping2=forms.CharField(label='Topping2',max_length=120)
#     size=forms.ChoiceField(label='size',choices=[['small','small'],['medium','medium'],['large','large']])
class Pizzaform(forms.ModelForm):
    # image=forms.ImageField()
    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
        labels={'topping1':'Topping 1','topping2':'Topping 2'}

class MultiplePizza(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=6)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
        