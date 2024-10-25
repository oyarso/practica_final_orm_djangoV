from django.db import models
import datetime

class Laboratorio(models.Model): 
    lab_id = models.AutoField(primary_key=True, verbose_name='ID')
    lab_nombre = models.CharField(max_length=255) 
    lab_ciudad= models.CharField(max_length=255,default="Santiago")
    lab_pais= models.CharField(max_length=255,default="Chile")
    def __str__(self): 
        return self.lab_nombre 

    
class DirectorGeneral(models.Model): 
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=255) 
    laboratorio =  models.OneToOneField(Laboratorio, on_delete=models.CASCADE) 
    especialidad = models.CharField(max_length=255, default="Medico General") 
    def __str__(self): 
        return self.nombre 
    
class Producto(models.Model): 
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=255) 
    laboratorio = models.ForeignKey(Laboratorio, 
    on_delete=models.SET_NULL, blank=True, null=True) 
    

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))


    f_fabricacion = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year)

    p_costo = models.DecimalField(max_digits=10, decimal_places=2) 
    p_venta = models.DecimalField(max_digits=10, decimal_places=2) 
    def __str__(self): 
        return self.nombre 
    

