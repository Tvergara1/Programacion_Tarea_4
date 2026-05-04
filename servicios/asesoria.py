from modelos.servicio import Servicio

class Asesoria(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        return 80 * horas

    def descripcion(self):
        return "Asesoría especializada"