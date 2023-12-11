from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(
        required=False, 
        max_length=35, 
        min_length=2, 
        label=False, 
        widget=forms.TextInput(
            attrs={"class":"form-input", 'placeholder':'Name'}
            )
        )
    



    email = forms.EmailField(
        required=False, 
        label=False, 
        widget=forms.EmailInput(
            attrs={"class":"form-input", 'placeholder':'Email'}
            )
        )
    



    phoneNum = forms.IntegerField(
        required=False, 
        label=False, 
        widget=forms.NumberInput(
            attrs={"class":"form-input", 'placeholder':'Phone number'}
            )
        )
    



    selectServ = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-input"}), 
        required=False, choices=(
            (1, 'Servise_1'), (2, 'Service_2'), (3, 'Service_3')
        ), 
        label=False)
    



    userComment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-textarea', 
                'placeholder':'Tell us about the car needing serivce(s)'
                }
            ), 
            required=False, 
            label=False)
    




class DeliveryForm(forms.Form):
    name = forms.CharField(
        required=False, 
        max_length=35, 
        min_length=2, 
        label=False, 
        widget=forms.TextInput(
            attrs={'placeholder':'Name'}
            )
        )
    
    surname = forms.CharField(
        required=False, 
        max_length=35, 
        min_length=2, 
        label=False, 
        widget=forms.TextInput(
            attrs={'placeholder':'Surname'}
            )
        )
    



    email = forms.CharField(
        required=False, 
        label=False, 
        widget=forms.EmailInput(
            attrs={'placeholder':'Email'}
            )
        )
    

    address = forms.CharField(
        required=False, 
        label=False, 
        widget=forms.TextInput(
            attrs={'placeholder':'Address'}
            )
        )


