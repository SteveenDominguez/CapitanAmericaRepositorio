from django import forms
from personaSalvada.models import PersonaSalvada
class PersonaSalvadaForm(forms.ModelForm):
    class Meta:
        model=PersonaSalvada

        fields=['id','nombre']
        labels={'Id': 'Id de la persona salvada'}
        widget={'Id':forms.TextInput()}
        labels={'Nombre':'Nombre de la persona salvada'}
        widget={'Nombre':forms.TextInput()}
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })