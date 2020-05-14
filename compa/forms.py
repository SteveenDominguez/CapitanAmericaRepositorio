from django import forms
from compa.models import Compa

class CompaForm(forms.ModelForm):
    class Meta:
        model=Compa

        fields=['id','nombre']
        labels={'Id': 'Id del compañero'}
        widget={'Id':forms.TextInput()}
        labels={'Nombre':'Nombre del compañero'}
        widget={'Nombre':forms.TextInput()}
        
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })