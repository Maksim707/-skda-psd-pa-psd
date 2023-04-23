from .models import Magicnumber, New
from django.forms import ModelForm, TextInput

class MagicForm(ModelForm):
    class Meta:
        model = Magicnumber
        fields = ['yrnum']
        widgets = {
            'yrnum': TextInput()
        }

class ForNews(ModelForm):
    class Meta:
        model = New
        fields = ['newtitle', "newdesc"]
        widget = {
            'newtitle': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите заголовок"

            }),
            'newdesc': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Введите описание"
            })
        }