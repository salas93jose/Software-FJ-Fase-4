
"""
Módulo: entidad.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define la clase abstracta Entidad, que sirve como base
para las entidades principales del sistema.
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self, identificador):
        """
        Constructor de la clase.

        Recibe un identificador único para cada entidad.
        """

        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacío.")

        self.__identificador = identificador.strip()

    @property
    def identificador(self):
        """
        Permite consultar el identificador sin modificarlo
        directamente.
        """
        return self.__identificador

    @abstractmethod
    def validar(self):
        """
        Método abstracto que cada clase hija debe implementar.

        Su función es validar la información de la entidad.
        """
        pass

    @abstractmethod
    def obtener_resumen(self):
        """
        Método abstracto que obliga a las clases hijas
        a proporcionar un resumen de su información.
        """
        pass
