from modelos.servicio import Servicio

class Sala(Servicio):

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        if horas <= 0:
            raise ValueError("Horas inválidas")
            
        costo = 50 * horas

        if descuento > 0:
        costo -= costo * descuento

    if impuesto > 0:
        costo += costo * impuesto

    return costo
        
        return 50 * horas

    def descripcion(self):
        return "Reserva de salas"