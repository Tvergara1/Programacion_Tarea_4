class Reserva:

    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "pendiente"

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo(self.horas)
            self.estado = "confirmada"
            return costo

        except Exception as e:
            raise Exception("Error en la reserva") from e

    def cancelar(self):
        self.estado = "cancelada"