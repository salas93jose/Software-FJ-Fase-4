
"""
Módulo: cliente.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define la clase Cliente, encargada de almacenar y
validar la información de los clientes.
"""

import re

from modelos.entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente del sistema Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):
        """
        Inicializa los datos del cliente.
        """

        super().__init__(identificador)

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        """
        Comprueba que los datos del cliente sean válidos.
        """

        if not isinstance(self.__nombre, str):
            raise ValueError("El nombre debe ser texto.")

        if not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s'-]{3,60}",
            self.__nombre.strip()
        ):
            raise ValueError("El nombre no es válido.")

        if not isinstance(self.__documento, str):
            raise ValueError("El documento debe ser texto.")

        if not re.fullmatch(r"\d{5,15}", self.__documento.strip()):
            raise ValueError("El documento debe contener entre 5 y 15 dígitos.")

        if not isinstance(self.__correo, str):
            raise ValueError("El correo debe ser texto.")

        patron_correo = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron_correo, self.__correo.strip()):
            raise ValueError("El correo electrónico no es válido.")

        if not isinstance(self.__telefono, str):
            raise ValueError("El teléfono debe ser texto.")

        telefono_limpio = re.sub(r"[\s()+-]", "", self.__telefono)

        if not telefono_limpio.isdigit() or not 7 <= len(telefono_limpio) <= 15:
            raise ValueError("El teléfono debe contener entre 7 y 15 dígitos.")

        return True

    def obtener_resumen(self):
        """
        Devuelve un resumen de la información del cliente.
        """

        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )
