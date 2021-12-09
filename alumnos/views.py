from django.shortcuts import render
from django.http import HttpResponse, response
import requests
import json 
from dotenv import load_dotenv



from alumnos.models import *



def alumnos(request):


    return render(request ,"Alumnos/alumnos.html")

def viewAlumnos(request):


    
    # alumnos =  listado.objects.all()
    alumnos =  listado.objects.all().order_by('id').reverse()
    diccionario = {
        "alumnos":alumnos
    }
 
    return render(request,"Alumnos/alumnos-suspendidos.html",diccionario)


def view_update_alumno(request,matricula):


    alumno  =  {}
    existe = True
    try:
        alumno  =  listado.objects.get(matricula=matricula)
    except :
        existe = False
        
    diccionario = {
        "alumno_seleccionado":alumno,
        "existe":existe,
        "matricula":matricula
    }
    return render(request,"Alumnos/vista-alumno.html",diccionario)



def agregar_alumno_form(request):

    
    return render(request,"Alumnos/agregar_alumno.html",{})


def agregar_alumno(request):

    alumno =  listado(name=request.POST.get("name")
    ,last_name=request.POST.get("last_name")
    ,email=request.POST.get("email")
    ,matricula=request.POST.get("matricula")
    ,age=request.POST.get("age")
    )
    guardado =  False
    if alumno.save():
        guardado = True
        
    return render(request,"Alumnos/agregar_alumno.html",context={"guardado":guardado})



def delete_alumnos(request, id_alumno):
    

    # if request.method == "GET":
        
    deleted = False
    message = ""
   
    try:
        alumno = listado.objects.get(id=id_alumno)
        alumno.delete()
        deleted = True
        message ="Alumno eliminado"
    except Exception as a:
        print(a)
        message="No se ha podido borrar el usuario"

    alumnos =  listado.objects.all().order_by('id').reverse()
    diccionario = {
        "alumnos":alumnos,
        "deleted":deleted,
        "message":message
    }
    return render(request,"Alumnos/alumnos-suspendidos.html",context=diccionario)
