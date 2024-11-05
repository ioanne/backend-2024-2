from django.db import models


class Carrera(models.Model):

    ESPECIALIDADES = (
        ("ingenieria", "Ingenieria"),
        ("medicina", "Medicina"),
        ("arte", "Arte"),
        ("derecho", "Derecho"),
    )

    nombre = models.CharField(max_length=50)
    duracion = models.PositiveIntegerField()
    descripcion = models.TextField()
    
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDADES, default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre

    @classmethod
    def obtener_carrera_ingenieria(cls):
        # Esta es la query que se ejecuta en la base de datos
        return cls.objects.filter(especialidad="ingenieria")
    
    def detalle(self):
        return f"{self.nombre} - {self.duracion} - {self.descripcion} - {self.especialidad}"
    

'''
class AutoFord:
    marca = "Ford"

    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
    
    def metodo(self):
        """Metodo de instancia"""
        return f"{self.marca} {self.modelo} {self.anio}"
    
    @classmethod
    def metodo_de_clase(cls):
        """Metodo de clase"""
        return cls.marca
    
    def metodo_de_clase2(cls):
        """Metodo de clase"""
        return cls.marca

    @staticmethod
    def metodo_estatico():
        """Metodo estatico"""
        return 2 + 2
    


AutoFord.metodo_de_clase()
AutoFord.metodo_estatico()

auto = AutoFord("Fiesta", 2020)
auto.metodo()
'''