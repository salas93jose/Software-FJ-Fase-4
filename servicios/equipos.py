
"""
Módulo: equipos.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define el servicio especializado de alquiler de
equipos tecnológicos.
"""

from modelos.servicio import Servicio


class Equipos(Servicio):
    """
    Representa el servicio de alquiler de equipos
    tecnológicos.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        tarifa_base,
        cantidad_disponible,
        tipo_equipo
    ):
        """
        Inicializa las características del servicio.
        """

        super().__init__(
            identificador,
            nombre,
            descripcion,
            tarifa_base
        )

        self.__cantidad_disponible = cantidad_disponible
        self.__tipo_equipo = tipo_equipo

        self.validar()

    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    def validar_parametros(self):
        """
        Valida la cantidad y el tipo de equipo.
        """

        if (
            isinstance(self.__cantidad_disponible, bool)
            or not isinstance(self.__cantidad_disponible, int)
            or self.__cantidad_disponible < 0
        ):
            raise ValueError(
                "La cantidad disponible debe ser un entero igual o mayor que cero."
            )

        if (
            not isinstance(self.__tipo_equipo, str)
            or not self.__tipo_equipo.strip()
        ):
            raise ValueError(
                "El tipo de equipo no puede estar vacío."
            )

        return True

    def calcular_costo(self, duracion, **opciones):
        """
        Calcula el alquiler según las horas y la cantidad
        de equipos solicitados.

        Permite aplicar un descuento opcional.
        """

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError(
                "La duración debe ser mayor que cero."
            )

        cantidad = opciones.get("cantidad", 1)
        descuento = opciones.get("descuento", 0)

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise ValueError(
                "La cantidad solicitada debe ser un entero mayor que cero."
            )

        if cantidad > self.__cantidad_disponible:
            raise ValueError(
                "No hay suficientes equipos disponibles."
            )

        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not 0 <= descuento <= 100
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

        costo = self.tarifa_base * duracion * cantidad
        costo_final = costo - (costo * descuento / 100)

        return costo_final

    def describir(self):
        """
        Devuelve una descripción del servicio de equipos.
        """

        return (
            f"{self.nombre} | "
            f"Tipo: {self.__tipo_equipo} | "
            f"Unidades disponibles: {self.__cantidad_disponible} | "
            f"Tarifa por hora y unidad: ${self.tarifa_base:,.0f} COP"
        )
