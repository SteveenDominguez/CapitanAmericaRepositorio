from django import forms
from enemigo.models import Enemigo
class EnemigoForm(forms.ModelForm):
    class Meta:
        model=Enemigo

        fields=['id','nombre']
        labels={'Id': 'Id del enemigo'}
        widget={'Id':forms.TextInput()}
        labels={'Nombre':'Nombre del enemigo'}
        widget={'Nombre':forms.TextInput()}
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })