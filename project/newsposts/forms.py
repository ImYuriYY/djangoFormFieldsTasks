from django import forms


class NewPost(forms.Form):
    title = forms.CharField(
        required=False, 
        label=False, 
        widget=forms.TextInput(
            attrs={"class":"new-post-title", 'placeholder':'Заголовок'}
            )
        )
    


    imag = forms.FileField(
        required=False,
        label=False,
    )
    

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'new-post-content', 
                'placeholder':'Контент'
                }
            ), 
            required=False, 
            label=False
        )


    isPublic = forms.ChoiceField(
        widget=forms.CheckboxInput(attrs={
                'class':'new-post-public-check'
                }),
        required=False,
        label='Публикация'
        )




    category = forms.ChoiceField(
    widget=forms.Select(attrs={"class":"new-post-category"}), 
    required=False, choices=(
        (1, 'Категория не выбрана'), (2, 'Категория 1'), (3, 'Категория 2')
    ), 
    label=False
    )