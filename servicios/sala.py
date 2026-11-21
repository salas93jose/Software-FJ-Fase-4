
"""
Módulo: sala.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define el servicio especializado de alquiler de salas.
"""

from modelos.servicio import Servicio


class Sala(Servicio):
    """
    Representa una sala disponible para alquiler.

    Hereda de la clase abstracta Servicio.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        tarifa_base,
        capacidad,
        tiene_proyector=False
    ):
        """
        Inicializa las características de la sala.
        """

        super().__init__(
            identificador,
            nombre,
            descripcion,
            tarifa_base
        )

        self.__capacidad = capacidad
        self.__tiene_proyector = tiene_proyector

        self.validar()

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def tiene_proyector(self):
        return self.__tiene_proyector

    def validar_parametros(self):
        """
        Valida las características particulares de la sala.
        """

        if (
            isinstance(self.__capacidad, bool)
            or not isinstance(self.__capacidad, int)
            or self.__capacidad <= 0
        ):
            raise ValueError(
                "La capacidad debe ser un número entero mayor que cero."
            )

        if not isinstance(self.__tiene_proyector, bool):
            raise ValueError(
                "La disponibilidad de proyector debe ser True o False."
            )

        return True

    def calcular_costo(self, duracion, **opciones):
        """
        Calcula el costo del alquiler según las horas reservadas.

        Puede aplicar un descuento opcional.
        """

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError(
                "La duración debe ser mayor que cero."
            )

        descuento = opciones.get("descuento", 0)

        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not 0 <= descuento <= 100
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

        costo = self.tarifa_base * duracion
        costo_final = costo - (costo * descuento / 100)

        return costo_final

    def describir(self):
        """
        Devuelve una descripción detallada de la sala.
        """

        proyector = (
            "Disponible" if self.__tiene_proyector
            else "No disponible"
        )

        return (
            f"{self.nombre} | "
            f"Capacidad: {self.__capacidad} personas | "
            f"Proyector: {proyector} | "
            f"Tarifa por hora: ${self.tarifa_base:,.0f} COP"
        )
