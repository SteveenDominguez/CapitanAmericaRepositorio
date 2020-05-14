from django.db import models
from patrocinador.models import Patrocinador
from aliado.models import Aliado

# Create your models here.
class Mision(models.Model):
    id = models.IntegerField( primary_key=True) 
    nombre = models.CharField(max_length=100,)
    fecha = models.DateField(auto_now=True)
    hora = models.CharField(max_length=100,)
    patrocinador =models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    aliado = models.ForeignKey(Aliado, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def __str__(self):
        return '{}'.format(self.hora)
    
    def save(self):
        
        super(Mision, self).save()

    class Meta:
        verbose_name_plural = "Misiones"