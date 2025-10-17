from typing import Dict


class Habitacion:
    """Representa una habitación del hotel."""

    ESTADOS_VALIDOS = {"disponible", "ocupada", "reservada"}

    def __init__(self, id_habitacion: int, tipo: str, precio: float, estado: str = "disponible"):
        self.id_habitacion = id_habitacion
        self.tipo = tipo
        self.precio = float(precio)
        self.estado = estado.lower()
        if self.estado not in self.ESTADOS_VALIDOS:
            # Si el estado no es válido, lo forzamos a 'disponible'
            self.estado = "disponible"

    def verificar_disponibilidad(self) -> bool:
        """Devuelve True si la habitación está disponible."""
        return self.estado == "disponible"

    def ocupar(self) -> bool:
        """
        Marca la habitación como 'ocupada' si está disponible.
        Devuelve True si la operación fue exitosa, False si no.
        """
        if self.verificar_disponibilidad():
            self.estado = "ocupada"
            return True
        return False

    def reservar(self) -> bool:
        """
        Marca la habitación como 'reservada' si está disponible.
        Devuelve True si la operación fue exitosa, False si no.
        """
        if self.verificar_disponibilidad():
            self.estado = "reservada"
            return True
        return False

    def liberar(self) -> None:
        """Libera la habitación y la deja como 'disponible'."""
        self.estado = "disponible"

    def actualizar_precio(self, nuevo_precio: float) -> None:
        """Actualiza el precio de la habitación (validando que sea positivo)."""
        try:
            p = float(nuevo_precio)
            if p < 0:
                raise ValueError("El precio no puede ser negativo.")
            self.precio = p
        except (TypeError, ValueError):
            raise ValueError("Precio inválido. Debe ser un número positivo.")

    def to_dict(self) -> Dict:
        """Devuelve un diccionario con la información de la habitación (útil para JSON / DB)."""
        return {
            "id_habitacion": self.id_habitacion,
            "tipo": self.tipo,
            "precio": self.precio,
            "estado": self.estado
        }

    def mostrar_en_consola(self) -> None:
        """Muestra la habitación en consola con formato elegante."""
        print("\n" + "=" * 40)
        print("          INFORMACIÓN DE HABITACIÓN")
        print("=" * 40)
        print(f"{'ID':15}: {self.id_habitacion}")
        print(f"{'Tipo':15}: {self.tipo}")
        print(f"{'Precio':15}: {self.precio}")
        print(f"{'Estado':15}: {self.estado}")
        print("=" * 40 + "\n")

    def __str__(self) -> str:
        return f"Habitacion#{self.id_habitacion} ({self.tipo}) - {self.estado} - {self.precio}"


# ---------------------------------------------------------
# Compatibilidad hacia atrás:
# Algunos archivos (ej. hotel.py) importan `habitacion` en minúscula.
# Para no romper imports antiguos, dejamos un alias:
# from habitaciones import habitacion
habitacion = Habitacion
