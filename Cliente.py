from typing import Dict, List


class Cliente:
    """Representa un cliente registrado en el sistema del Hotel Sena."""

    def __init__(self, id_cliente: int, nombre: str, correo: str, telefono: int):
        self.id_cliente = id_cliente
        self.nombre = nombre.strip().title()
        self.correo = correo.strip().lower()
        self.telefono = str(telefono).strip()
        self.reservas: List[Dict] = []  # historial de reservas (lista de diccionarios)

        # Validaciones personalizadas
        if not self._validar_nombre(self.nombre):
            raise ValueError("El nombre no puede estar vacío o contener solo espacios.")
        if not self._validar_correo(self.correo):
            raise ValueError("Correo inválido: debe contener '@' y 'gmail.com'.")
        if not self._validar_telefono(self.telefono):
            raise ValueError("Número de teléfono inválido: debe tener exactamente 10 dígitos.")

    # ----------------------------------------------------------
    # Métodos privados de validación
    # ----------------------------------------------------------
    def _validar_nombre(self, nombre: str) -> bool:
        """Valida que el nombre no esté vacío."""
        return bool(nombre and nombre.strip())

    def _validar_correo(self, correo: str) -> bool:
        """Valida que el correo contenga '@' y 'gmail.com'."""
        return "@" in correo and "gmail.com" in correo

    def _validar_telefono(self, telefono: str) -> bool:
        """Valida que el teléfono tenga exactamente 10 dígitos."""
        return telefono.isdigit() and len(telefono) == 10

    # ----------------------------------------------------------
    # Métodos funcionales
    # ----------------------------------------------------------
    def registrar_reserva(self, reserva: Dict) -> None:
        """Agrega una reserva al historial del cliente."""
        self.reservas.append(reserva)
        print(f"Reserva registrada correctamente para {self.nombre}.")

    def actualizar_info(self, nombre: str = None, correo: str = None, telefono: int = None) -> None:
        """Permite actualizar los datos del cliente."""
        if nombre:
            if self._validar_nombre(nombre):
                self.nombre = nombre.strip().title()
            else:
                print("Error: el nombre no puede estar vacío.")
        if correo:
            if self._validar_correo(correo):
                self.correo = correo.strip().lower()
            else:
                print("Error: el correo debe contener '@' y 'gmail.com'.")
        if telefono:
            if self._validar_telefono(str(telefono)):
                self.telefono = str(telefono)
            else:
                print("Error: el teléfono debe tener exactamente 10 dígitos.")
        print(f"Información actualizada correctamente para el cliente #{self.id_cliente}.")

    def consultar_info(self) -> Dict:
        """Devuelve la información completa del cliente como diccionario."""
        return {
            "ID": self.id_cliente,
            "Nombre": self.nombre,
            "Correo": self.correo,
            "Teléfono": self.telefono,
            "Reservas": len(self.reservas)
        }

    def mostrar_en_consola(self) -> None:
        """Muestra la información del cliente en formato elegante."""
        print("\n" + "=" * 40)
        print("        INFORMACIÓN DEL CLIENTE")
        print("=" * 40)
        print(f"{'ID':15}: {self.id_cliente}")
        print(f"{'Nombre':15}: {self.nombre}")
        print(f"{'Correo':15}: {self.correo}")
        print(f"{'Teléfono':15}: {self.telefono}")
        print(f"{'Reservas':15}: {len(self.reservas)} registradas")
        print("=" * 40 + "\n")

    def __str__(self) -> str:
        """Representación simple en texto del cliente."""
        return f"{self.nombre} ({self.correo})"
