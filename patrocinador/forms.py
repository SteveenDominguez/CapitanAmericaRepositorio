from django import forms
from patrocinador.models import Patrocinador
class PatrocinadorForm(forms.ModelForm):
    class Meta:
        model=Patrocinador

        fields=['id','nombre','dinero']
        labels={'Id': 'Id del patrocinador'}
        widget={'Id':forms.TextInput()}
        labels={'Nombre':'Nombre del patrocinador'}
        widget={'Nombre':forms.TextInput()}
        labels={'Dinero': 'Dinero del patrocinador'}
        widget={'Dinero':forms.TextInput()}
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })