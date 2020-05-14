from django import forms
from mision.models import Mision
class MisionForm(forms.ModelForm):
    class Meta:
        model=Mision

        fields=['id','nombre','hora','patrocinador','aliado']
        labels={'Id': 'Id de la Mision'}
        widget={'Id':forms.TextInput()}
        labels={'Nombre':'Nombre de la Mision'}
        widget={'Nombre':forms.TextInput()}
        labels={'Hora':'Hora de la mision'}
        widget={'Hora':forms.TextInput()}
        labels={'Id_Aliado':'Id del Aliado de la Mision'}
        widget={'Id_Aliado':forms.TextInput()}
        labels={'Id_Patrocinador':'Id del Patrocinador de la Mision'}
        widget={'Id_Patrocinador':forms.TextInput()}
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })