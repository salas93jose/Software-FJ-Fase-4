
"""
Módulo principal: main.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Integra los clientes, servicios y reservas
mediante un menú interactivo.
"""

from pathlib import Path

from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.sala import Sala
from servicios.equipos import Equipos
from servicios.asesoria import Asesoria

from utilidades.excepciones import ErrorReserva
from utilidades.registro_logs import registrar_evento, registrar_error


# Listas internas para almacenar la información
clientes = []
servicios = []
reservas = []


def cargar_servicios():
    """
    Registra los servicios disponibles en el sistema.
    """

    servicios.append(
        Sala(
            "SAL001",
            "Sala de reuniones",
            "Espacio para reuniones empresariales",
            50000,
            20,
            True
        )
    )

    servicios.append(
        Equipos(
            "EQ001",
            "Alquiler de computadores",
            "Equipos portátiles para actividades empresariales",
            20000,
            10,
            "Computador portátil"
        )
    )

    servicios.append(
        Asesoria(
            "ASE001",
            "Asesoría tecnológica",
            "Orientación en infraestructura y sistemas informáticos",
            60000,
            "Tecnología",
            "Carlos Ramírez"
        )
    )

    registrar_evento("Servicios iniciales cargados correctamente.")


def mostrar_menu():
    """
    Presenta las opciones principales del sistema.
    """

    print("\n" + "=" * 55)
    print("       SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 55)
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Consultar servicios")
    print("4. Crear reserva")
    print("5. Confirmar reserva")
    print("6. Cancelar reserva")
    print("7. Procesar reserva")
    print("8. Consultar reservas")
    print("9. Consultar registros del sistema")
    print("10. Salir")
    print("=" * 55)


def registrar_cliente():
    """
    Solicita los datos y registra un nuevo cliente.
    """

    print("\n--- REGISTRO DE CLIENTE ---")

    try:
        nombre = input("Nombre completo: ").strip()
        documento = input("Documento: ").strip()
        correo = input("Correo electrónico: ").strip()
        telefono = input("Teléfono: ").strip()

        identificador = f"CLI{len(clientes) + 1:03d}"

        cliente = Cliente(
            identificador,
            nombre,
            documento,
            correo,
            telefono
        )

        clientes.append(cliente)

    except (ValueError, TypeError) as error:
        registrar_error(f"Error al registrar cliente: {error}")
        print("\nNo fue posible registrar el cliente:", error)

    else:
        registrar_evento(
            f"Cliente {identificador} registrado correctamente."
        )

        print("\nCliente registrado exitosamente.")
        print(cliente.obtener_resumen())

    finally:
        registrar_evento("Finalizó el proceso de registro de cliente.")


def consultar_clientes():
    """
    Muestra los clientes registrados.
    """

    print("\n--- CLIENTES REGISTRADOS ---")

    if not clientes:
        print("Todavía no hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente.obtener_resumen())


def consultar_servicios():
    """
    Muestra los servicios disponibles.
    """

    print("\n--- SERVICIOS DISPONIBLES ---")

    for indice, servicio in enumerate(servicios, start=1):
        print(f"\n{indice}. {servicio.obtener_resumen()}")
        print(servicio.describir())


def seleccionar_cliente():
    """
    Permite seleccionar un cliente por su número.
    """

    if not clientes:
        print("Primero debe registrar un cliente.")
        return None

    consultar_clientes()

    try:
        numero = int(input("\nSeleccione el número del cliente: "))

        if numero < 1 or numero > len(clientes):
            registrar_error("Selección de cliente no válida.")
            print("Selección de cliente no válida.")
            return None

        return clientes[numero - 1]

    except ValueError as error:
        registrar_error(f"Error al seleccionar cliente: {error}")
        print("Debe ingresar un número entero.")
        return None


def seleccionar_servicio():
    """
    Permite seleccionar uno de los servicios disponibles.
    """

    consultar_servicios()

    try:
        numero = int(input("\nSeleccione el número del servicio: "))

        if numero < 1 or numero > len(servicios):
            registrar_error("Selección de servicio no válida.")
            print("Selección de servicio no válida.")
            return None

        return servicios[numero - 1]

    except ValueError as error:
        registrar_error(f"Error al seleccionar servicio: {error}")
        print("Debe ingresar un número entero.")
        return None


def crear_reserva():
    """
    Crea una reserva asociando un cliente con un servicio.
    Si el servicio corresponde a equipos, solicita
    la cantidad de unidades necesarias.
    """

    print("\n--- CREAR RESERVA ---")

    cliente = seleccionar_cliente()

    if cliente is None:
        return

    servicio = seleccionar_servicio()

    if servicio is None:
        return

    try:
        duracion = float(input("\nDuración en horas: "))

        opciones = {}

        if isinstance(servicio, Equipos):
            cantidad = int(
                input("Cantidad de equipos que desea reservar: ")
            )

            opciones["cantidad"] = cantidad

        identificador = f"RES{len(reservas) + 1:03d}"

        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion,
            **opciones
        )

        reservas.append(reserva)

    except (ErrorReserva, ValueError, TypeError) as error:
        registrar_error(f"Error al crear reserva: {error}")

        if isinstance(error, ErrorReserva) and error.__cause__:
            print(
                "\nNo fue posible crear la reserva:",
                error.__cause__
            )
        else:
            print(
                "\nNo fue posible crear la reserva:",
                error
            )

    else:
        print("\nReserva creada exitosamente.")
        print(reserva.obtener_resumen())


def buscar_reserva():
    """
    Busca una reserva mediante su identificador.
    """

    if not reservas:
        print("No hay reservas registradas.")
        return None

    identificador = input(
        "\nIngrese el identificador de la reserva: "
    ).strip().upper()

    for reserva in reservas:
        if reserva.identificador == identificador:
            return reserva

    registrar_error(
        f"No se encontró la reserva {identificador}."
    )
    print("No se encontró la reserva indicada.")
    return None


def confirmar_reserva():
    """
    Confirma una reserva pendiente.
    """

    print("\n--- CONFIRMAR RESERVA ---")

    reserva = buscar_reserva()

    if reserva is None:
        return

    try:
        reserva.confirmar()
        print("Reserva confirmada correctamente.")

    except ErrorReserva as error:
        registrar_error(f"Error al confirmar reserva: {error}")
        print("No fue posible confirmar:", error)


def cancelar_reserva():
    """
    Cancela una reserva pendiente o confirmada.
    """

    print("\n--- CANCELAR RESERVA ---")

    reserva = buscar_reserva()

    if reserva is None:
        return

    try:
        reserva.cancelar()
        print("Reserva cancelada correctamente.")

    except ErrorReserva as error:
        registrar_error(f"Error al cancelar reserva: {error}")
        print("No fue posible cancelar:", error)


def procesar_reserva():
    """
    Procesa una reserva previamente confirmada.
    """

    print("\n--- PROCESAR RESERVA ---")

    reserva = buscar_reserva()

    if reserva is None:
        return

    try:
        reserva.procesar()
        print("Reserva procesada correctamente.")

    except ErrorReserva as error:
        registrar_error(f"Error al procesar reserva: {error}")
        print("No fue posible procesar:", error)


def consultar_reservas():
    """
    Muestra todas las reservas registradas.
    """

    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("Todavía no hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.obtener_resumen())


def consultar_logs():
    """
    Muestra el contenido del archivo de registros.
    """

    print("\n--- REGISTROS DEL SISTEMA ---")

    ruta_logs = (
        Path(__file__).resolve().parent
        / "logs"
        / "software_fj.log"
    )

    if not ruta_logs.exists():
        print("Todavía no existe un archivo de registros.")
        return

    contenido = ruta_logs.read_text(encoding="utf-8")

    if contenido.strip():
        print(contenido)
    else:
        print("No hay registros disponibles.")


def iniciar_sistema():
    """
    Ejecuta el menú principal de Software FJ.
    """

    cargar_servicios()

    registrar_evento("Sistema Software FJ iniciado.")

    print("\nBienvenido al sistema Software FJ.")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            consultar_clientes()

        elif opcion == "3":
            consultar_servicios()

        elif opcion == "4":
            crear_reserva()

        elif opcion == "5":
            confirmar_reserva()

        elif opcion == "6":
            cancelar_reserva()

        elif opcion == "7":
            procesar_reserva()

        elif opcion == "8":
            consultar_reservas()

        elif opcion == "9":
            consultar_logs()

        elif opcion == "10":
            registrar_evento("Sistema Software FJ finalizado.")
            print("\nGracias por utilizar Software FJ.")
            break

        else:
            registrar_error(
                f"Opción de menú no válida: {opcion}"
            )
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    iniciar_sistema()
