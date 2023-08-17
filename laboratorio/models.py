from django.core.exceptions import ValidationError
from django.db import models
from datetime import MINYEAR
from .apps import LaboratorioConfig
# Create your models here.

class Laboratorio(models.Model):
    id= models.AutoField(primary_key=True)
    lab_nombre = models.CharField(max_length=200)
    lab_ciudad= models.CharField(max_length=100, null=True)
    lab_pais= models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = "laboratorio"
        verbose_name_plural = "Laboratorios"
        ordering = ['-id']
        db_table= 'laboratorio'

    def __str__(self):
        return str(self.id)

class DirectorGeneral(models.Model):
    id_dir = models.AutoField(primary_key=True)
    dir_nombre = models.CharField(max_length=200)
    laboratorio = models.OneToOneField(Laboratorio, models.DO_NOTHING, db_column='lab_nombre', blank=True, null=True, unique=True)
    especialidad= models.CharField(max_length=30, null=True)

    class Meta:
        
        verbose_name_plural = "Directores Generales"
        db_table= 'directorgeneral'

    

def Min_year(value):
    if value.year < 2015:
        raise ValidationError('El año de fabricacion no puede ser anterior al año 2015.')

class Producto(models.Model):
    id= models.AutoField(primary_key=True,)
    pro_nombre = models.CharField(max_length=200, unique=True)
    pro_laboratorio = models.OneToOneField(Laboratorio, models.DO_NOTHING, db_column='lab_nombre', blank=True, null=True)
    f_fabricacion = models.DateField(validators=[Min_year])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'producto'

 