from django import forms
from aliado.models import Aliado
class AliadoForm(forms.ModelForm):
    class Meta:
        model=Aliado

        fields=['id','nombre']
        labels={'Id': 'Id del aliado'}
        widget={'Id':forms.TextInput()}
        labels={'Nombre':'Nombre del Aliado'}
        widget={'Nombre':forms.TextInput()}
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })