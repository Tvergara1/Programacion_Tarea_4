# Sistema de Gestión - Software FJ

#  Descripción del Proyecto

Este proyecto corresponde al desarrollo de un sistema integral orientado a objetos para la empresa ficticia *Software FJ*, encargado de gestionar clientes, servicios y reservas.

El sistema ha sido desarrollado en Python sin uso de bases de datos, utilizando únicamente estructuras de datos en memoria y archivos para el registro de eventos y errores.

---

#  Objetivo

Construir una aplicación modular, extensible y robusta que implemente correctamente los principios de la Programación Orientada a Objetos (POO), incluyendo:

- Abstracción  
- Herencia  
- Polimorfismo  
- Encapsulación  
- Manejo avanzado de excepciones  

---

# Estructura del Proyecto

software-fj-sistema/
│
├── main.py  
├── logs.txt  
│  
├── modelos/  
│   ├── cliente.py  
│   ├── entidad.py  
│   ├── reserva.py  
│  
├── servicios/  
│   ├── sala.py  
│   ├── equipo.py  
│   ├── asesoria.py  
│  
├── excepciones/  
│   └── errores.py  
│  
├── utils/  
│   └── logger.py  

---

# Funcionalidades

- Registro de clientes con validaciones estrictas  
- Gestión de servicios (salas, equipos y asesorías)  
- Creación y gestión de reservas  
- Cálculo de costos con polimorfismo  
- Manejo de errores personalizados  
- Registro de logs de eventos y excepciones  
- Simulación de operaciones válidas e inválidas  

---

# Manejo de Excepciones

El sistema implementa:

- try / except  
- try / except / else  
- try / except / finally  
- Excepciones personalizadas  
- Encadenamiento de excepciones  
- Registro de errores en archivo logs.txt  

---

#  Simulación del Sistema

El programa incluye al menos 10 operaciones simuladas, combinando:

- Creación de clientes válidos e inválidos  
- Servicios correctamente instanciados y con errores  
- Reservas exitosas y fallidas  
- Manejo continuo de errores sin detener el sistema  

---

#  Ejecución

Para ejecutar el sistema:

```bash
python main.py