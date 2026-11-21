
"""
Módulo: reserva.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define la clase Reserva, que relaciona clientes
con servicios y administra el ciclo de vida
de cada reserva.
"""

from modelos.entidad import Entidad
from modelos.cliente import Cliente
from modelos.servicio import Servicio

from utilidades.excepciones import ErrorReserva
from utilidades.registro_logs import registrar_evento, registrar_error


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente.
    """

    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    PROCESADA = "PROCESADA"

    def __init__(self, identificador, cliente, servicio, duracion, **opciones):
        """
        Inicializa una reserva con su cliente,
        servicio, duración y opciones adicionales.
        """

        super().__init__(identificador)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = self.PENDIENTE
        self.__costo = 0
        self.__opciones = opciones.copy()

        try:
            self.validar()

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                **self.__opciones
            )

        except (ValueError, TypeError) as error:
            registrar_error(
                f"Error al crear la reserva {identificador}: {error}"
            )
            raise ErrorReserva(
                "No fue posible crear la reserva. Verifique los datos."
            ) from error

        registrar_evento(
            f"Reserva {self.identificador} creada correctamente."
        )

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def validar(self):
        """
        Comprueba que el cliente, el servicio
        y la duración sean válidos.
        """

        if not isinstance(self.__cliente, Cliente):
            raise ValueError(
                "La reserva debe estar asociada a un cliente válido."
            )

        if not isinstance(self.__servicio, Servicio):
            raise ValueError(
                "La reserva debe estar asociada a un servicio válido."
            )

        if (
            isinstance(self.__duracion, bool)
            or not isinstance(self.__duracion, (int, float))
            or self.__duracion <= 0
        ):
            raise ValueError(
                "La duración de la reserva debe ser mayor que cero."
            )

        return True

    def obtener_resumen(self):
        """
        Devuelve un resumen completo de la reserva.
        """

        resumen = (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duración: {self.__duracion} horas | "
        )

        if "cantidad" in self.__opciones:
            resumen += (
                f"Cantidad de equipos: {self.__opciones['cantidad']} | "
            )

        resumen += (
            f"Costo: ${self.__costo:,.0f} COP | "
            f"Estado: {self.__estado}"
        )

        return resumen

    def confirmar(self):
        """
        Confirma una reserva que se encuentre pendiente.
        """

        if self.__estado != self.PENDIENTE:
            mensaje = (
                f"No se puede confirmar la reserva {self.identificador}. "
                f"Su estado actual es {self.__estado}."
            )
            registrar_error(mensaje)
            raise ErrorReserva(mensaje)

        self.__estado = self.CONFIRMADA

        registrar_evento(
            f"Reserva {self.identificador} confirmada."
        )

        return True

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.
        """

        if self.__estado not in (self.PENDIENTE, self.CONFIRMADA):
            mensaje = (
                f"No se puede cancelar la reserva {self.identificador}. "
                f"Su estado actual es {self.__estado}."
            )
            registrar_error(mensaje)
            raise ErrorReserva(mensaje)

        self.__estado = self.CANCELADA

        registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

        return True

    def procesar(self):
        """
        Finaliza una reserva que haya sido confirmada.
        """

        if self.__estado != self.CONFIRMADA:
            mensaje = (
                f"No se puede procesar la reserva {self.identificador}. "
                "Primero debe estar confirmada."
            )
            registrar_error(mensaje)
            raise ErrorReserva(mensaje)

        self.__estado = self.PROCESADA

        registrar_evento(
            f"Reserva {self.identificador} procesada correctamente."
        )

        return True
