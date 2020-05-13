from django import forms
from companeros.models import Companeros

class CompanerosForm(forms.ModelForm):
    class Meta:
        model=Companeros

        fields=['id','nombre','dinero']
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