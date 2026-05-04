from modelos.servicio import Servicio

class Equipo(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        return 30 * horas

    def descripcion(self):
        return "Alquiler de equipos"