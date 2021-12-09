from django.db import models
from django.db.models.fields import CharField, EmailField
from  datetime import datetime

# Create your models here.
class listado(models.Model):
    name =  models.CharField(max_length=150)
    last_name =  models.CharField(max_length=150)
    email =  models.EmailField (max_length=254)
    age =  models.BigIntegerField(null=True)
    matricula = models.CharField(max_length=15)
    created_at =  models.DateTimeField(default=datetime.now,blank=True)
    updated_at =  models.DateTimeField(default=datetime.now,blank=True)

class materias(models.Model):
    name =  models.CharField(max_length=150)
    maestro =  models.CharField(max_length=70,null=True)
    creditos =  models.DecimalField(max_digits=3,decimal_places=2)
    created_at =  models.DateTimeField(default=datetime.now,blank=True)
    updated_at =  models.DateTimeField(default=datetime.now,blank=True)

    
        
class calificaciones(models.Model):
    alumno = models.ForeignKey(listado,on_delete=models.CASCADE)
    materia  =  models.ForeignKey(materias,on_delete=models.CASCADE)
    calificacion  =  models.DecimalField(max_digits=2,decimal_places=2)
    created_at =  models.DateTimeField(default=datetime.now,blank=True)
    updated_at =  models.DateTimeField(default=datetime.now,blank=True)




        
        