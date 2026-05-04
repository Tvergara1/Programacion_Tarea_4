from modelos.cliente import Cliente
from servicios.sala import Sala
from servicios.equipo import Equipo
from servicios.asesoria import Asesoria
from modelos.reserva import Reserva
from utils.logger import log_error, log_event

def main():

    operaciones = []

    # 1 cliente válido
    try:
        c1 = Cliente("Juan", "juan@mail.com")
        operaciones.append("cliente válido")
    except Exception as e:
        log_error(str(e))

    # 2 cliente inválido
    try:
        c2 = Cliente("", "error")
    except Exception as e:
        log_error(str(e))

    # 3 sala OK
    try:
        servicio = Sala("Sala VIP")
        r1 = Reserva(c1, servicio, 3)
        operaciones.append(r1.confirmar())
    except Exception as e:
        log_error(str(e))

    # 4 reserva inválida
    try:
        r2 = Reserva(c1, servicio, -2)
        r2.confirmar()
    except Exception as e:
        log_error(str(e))

    # 5 equipo
    try:
        eq = Equipo("Proyector")
        r3 = Reserva(c1, eq, 2)
        operaciones.append(r3.confirmar())
    except Exception as e:
        log_error(str(e))

    # 6 asesoría
    try:
        aseso = Asesoria("IA Consulting")
        r4 = Reserva(c1, aseso, 1)
        operaciones.append(r4.confirmar())
    except Exception as e:
        log_error(str(e))

    # 7 cancelación
    try:
        r4.cancelar()
        operaciones.append("cancelada")
    except Exception as e:
        log_error(str(e))

    # 8 error forzado
    try:
        x = 1 / 0
    except Exception as e:
        log_error("division por cero")

    # 9 operación válida extra
    try:
        r5 = Reserva(c1, servicio, 5)
        operaciones.append(r5.confirmar())
    except Exception as e:
        log_error(str(e))

    # 10 cliente válido 2
    try:
        c3 = Cliente("Maria", "maria@mail.com")
        operaciones.append("cliente 2 OK")
    except Exception as e:
        log_error(str(e))

    print("OPERACIONES:", operaciones)


if __name__ == "__main__":
    main()