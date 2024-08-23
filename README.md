# backend-2024-2

## Como hacer funcionar el proyecto

Crear un entorno virtual usando

```
python -m venv env
```

## luego, ingresamos al enterno virtual

### Ubuntu

source ./env/bin/activate

### Windows

.\env\Scripts\activate

### Desactivarlo

deactivate

### Instalar dependencias

```
pip install -r requirements.txt
```

### django-admin

Lo vamos a usar unicamente para estos sub comandos:
startproject

django-admin startaproject <nombre_proyecto>

cd <nombre_proyecto>
django-admin startapp <nombre_aplicacion>

startapp

Es decir, esto nos va a permitir crear "archivos y carpetas" de django

### python manage.py

Este comando se va a usar una vez que tengamos django creado con todas nuestras apps.
