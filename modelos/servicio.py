from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre):
        if not nombre:
            raise ValueError("Nombre de servicio inválido")
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass