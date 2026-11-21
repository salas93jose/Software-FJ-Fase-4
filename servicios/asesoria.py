
"""
Módulo: asesoria.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define el servicio especializado de asesorías.
"""

from modelos.servicio import Servicio


class Asesoria(Servicio):
    """
    Representa un servicio de asesoría especializada.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        tarifa_base,
        tipo_asesoria,
        profesional
    ):
        """
        Inicializa las características de la asesoría.
        """

        super().__init__(
            identificador,
            nombre,
            descripcion,
            tarifa_base
        )

        self.__tipo_asesoria = tipo_asesoria
        self.__profesional = profesional

        self.validar()

    @property
    def tipo_asesoria(self):
        return self.__tipo_asesoria

    @property
    def profesional(self):
        return self.__profesional

    def validar_parametros(self):
        """
        Valida el tipo de asesoría y el profesional encargado.
        """

        if (
            not isinstance(self.__tipo_asesoria, str)
            or not self.__tipo_asesoria.strip()
        ):
            raise ValueError(
                "El tipo de asesoría no puede estar vacío."
            )

        if (
            not isinstance(self.__profesional, str)
            or not self.__profesional.strip()
        ):
            raise ValueError(
                "El nombre del profesional no puede estar vacío."
            )

        return True

    def calcular_costo(self, duracion, **opciones):
        """
        Calcula el costo de la asesoría según su duración.

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
        Devuelve una descripción detallada de la asesoría.
        """

        return (
            f"{self.nombre} | "
            f"Tipo de asesoría: {self.__tipo_asesoria} | "
            f"Profesional: {self.__profesional} | "
            f"Tarifa por hora: ${self.tarifa_base:,.0f} COP"
        )
