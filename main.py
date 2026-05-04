#*******************************************#
# Tarea Programacion Fase 4                 #
# Aqui tenemos la parte MAIN del proyecto,  #
# desde donde se desprendera el resto de la #
# arquitectura.                             #
#*******************************************#
from modelos.cliente import Cliente
from servicios.sala import Sala
from servicios.equipo import Equipo
from servicios.asesoria import Asesoria
from modelos.reserva import Reserva
from utils.logger import log_error

def main():

    operaciones = []

    # =========================
    # 1. Cliente válido
    # =========================
    try:
        c1 = Cliente("Juan", "juan@mail.com")
        operaciones.append("Cliente válido creado")
    except Exception as e:
        log_error(str(e))

    # =========================
    # 2. Cliente inválido
    # =========================
    try:
        c2 = Cliente("", "error")  # falla
    except Exception as e:
        log_error("Cliente inválido: " + str(e))

    # =========================
    # 3. Cliente válido 2
    # =========================
    try:
        c3 = Cliente("Maria", "maria@mail.com")
        operaciones.append("Cliente 2 creado")
    except Exception as e:
        log_error(str(e))

    # =========================
    # 4. Servicio sala
    # =========================
    try:
        sala = Sala("Sala VIP")
        operaciones.append(sala.descripcion())
    except Exception as e:
        log_error(str(e))

    # =========================
    # 5. Servicio equipo
    # =========================
    try:
        equipo = Equipo("Proyector")
        operaciones.append(equipo.descripcion())
    except Exception as e:
        log_error(str(e))

    # =========================
    # 6. Servicio asesoría
    # =========================
    try:
        asesoria = Asesoria("IA Consulting")
        operaciones.append(asesoria.descripcion())
    except Exception as e:
        log_error(str(e))

    # =========================
    # 7. Reserva exitosa
    # =========================
    try:
        r1 = Reserva(c1, sala, 3)
        costo = r1.confirmar()
        operaciones.append(f"Reserva OK: {costo}")
    except Exception as e:
        log_error(str(e))

    # =========================
    # 8. Reserva inválida
    # =========================
    try:
        r2 = Reserva(c1, sala, -5)
        r2.confirmar()
    except Exception as e:
        log_error("Reserva inválida: " + str(e))

    # =========================
    # 9. Error forzado
    # =========================
    try:
        x = 1 / 0
    except Exception as e:
        log_error("Error controlado: división por cero")

    # =========================
    # 10. Reserva equipo
    # =========================
    try:
        r3 = Reserva(c3, equipo, 2)
        operaciones.append(f"Reserva equipo: {r3.confirmar()}")
    except Exception as e:
        log_error(str(e))

    # Resultado final
    print("\nOPERACIONES:")
    for op in operaciones:
        print("-", op)


if __name__ == "__main__":
    main()