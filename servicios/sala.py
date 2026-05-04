from modelos.servicio import Servicio

class Sala(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        return 50 * horas

    def descripcion(self):
        return "Reserva de salas"