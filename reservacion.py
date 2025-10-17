import json
import os
from datetime import datetime

class Reservacion:
    """Clase que representa una reservación de hotel."""

    def __init__(self, id_reserva, cliente, habitacion, fecha_ingreso, fecha_salida, precio, estado="activa"):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion

        # Validación de fechas
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        self.fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
        if self.fecha_salida <= self.fecha_ingreso:
            raise ValueError(" La fecha de salida debe ser posterior a la de ingreso.")

        self.precio = precio
        self.estado = estado.lower()

        # Cambiar estado de la habitación automáticamente
        if self.habitacion.estado.lower() == "disponible":
            self.habitacion.estado = "reservada"

    def calcular_precio_total(self):
        """Calcula el costo total según los días de estadía."""
        dias = (self.fecha_salida - self.fecha_ingreso).days
        return dias * self.precio

    def cancelar(self):
        """Cancela la reservación si está activa."""
        if self.estado == "activa":
            self.estado = "cancelada"
            self.habitacion.estado = "disponible"
            print(f" Reservación #{self.id_reserva} cancelada correctamente.")
        else:
            print(f"La reservación #{self.id_reserva} ya estaba cancelada.")

    def mostrar_reservacion(self):
        """Devuelve los datos de la reservación como diccionario."""
        return {
            "ID": self.id_reserva,
            "Cliente": self.cliente.nombre,
            "Habitación": self.habitacion.id_habitacion,
            "Ingreso": self.fecha_ingreso.strftime("%Y-%m-%d"),
            "Salida": self.fecha_salida.strftime("%Y-%m-%d"),
            "Precio por día": self.precio,
            "Precio total": self.calcular_precio_total(),
            "Estado": self.estado
        }

    def mostrar_en_consola(self):
        """Muestra la reservación en formato elegante."""
        info = self.mostrar_reservacion()
        print("\n" + "="*40)
        print("         RESERVACIÓN DE HOTEL")
        print("="*40)
        for k, v in info.items():
            print(f"{k:15}: {v}")
        print("="*40 + "\n")

    def guardar_json(self, ruta_archivo="data/reservas.json"):
        """Guarda la reservación en un archivo JSON (crea carpeta si no existe)."""
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

        data = []
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

        data.append(self.mostrar_reservacion())

        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f" Reservación #{self.id_reserva} guardada correctamente en {ruta_archivo}")
