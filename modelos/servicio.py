
"""
Módulo: servicio.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define la clase abstracta Servicio, que establece
la estructura común de los servicios ofrecidos.
"""

from abc import abstractmethod

from modelos.entidad import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio general.
    Hereda de Entidad.
    """

    def __init__(self, identificador, nombre, descripcion, tarifa_base):
        """
        Inicializa los datos generales del servicio.
        """

        super().__init__(identificador)

        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__tarifa_base = tarifa_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def tarifa_base(self):
        return self.__tarifa_base

    def validar(self):
        """
        Valida los datos generales del servicio
        y los parámetros específicos de cada servicio.
        """

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        if not isinstance(self.__descripcion, str) or not self.__descripcion.strip():
            raise ValueError("La descripción del servicio no puede estar vacía.")

        if (
            isinstance(self.__tarifa_base, bool)
            or not isinstance(self.__tarifa_base, (int, float))
            or self.__tarifa_base <= 0
        ):
            raise ValueError("La tarifa base debe ser un número mayor que cero.")

        self.validar_parametros()

        return True

    def obtener_resumen(self):
        """
        Devuelve la información general del servicio.
        """

        return (
            f"Servicio: {self.__nombre} | "
            f"Descripción: {self.__descripcion} | "
            f"Tarifa base: ${self.__tarifa_base:,.0f} COP"
        )

    @abstractmethod
    def calcular_costo(self, duracion, **opciones):
        """
        Calcula el costo del servicio.

        Cada servicio especializado implementará
        su propia fórmula de cálculo.
        """
        pass

    @abstractmethod
    def describir(self):
        """
        Devuelve una descripción específica del servicio.
        """
        pass

    @abstractmethod
    def validar_parametros(self):
        """
        Comprueba los parámetros particulares del servicio.
        """
        pass
