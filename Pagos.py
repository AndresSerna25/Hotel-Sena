import time
import random
import json
import os

class Pago:
    """Representa el pago asociado a una reservación."""

    METODOS_VALIDOS = ["tarjeta", "nequi", "daviplata", "paypal"]

    def __init__(self, id_pago, monto, metodo_pago):
        self.id_pago = id_pago
        self.monto = float(monto)
        self.metodo_pago = metodo_pago.strip().lower()
        self.estado = "pendiente"

    # ----------------------------------------------------------
    # Validación del método de pago
    # ----------------------------------------------------------
    def validar_metodo_pago(self):
        """Verifica que el método de pago sea válido."""
        if self.metodo_pago in self.METODOS_VALIDOS:
            print(f"Método de pago '{self.metodo_pago}' válido.")
            return True
        else:
            print(f"Método de pago '{self.metodo_pago}' no es válido.")
            self.estado = "rechazado"
            return False

    # ----------------------------------------------------------
    # Proceso de pago (simulación)
    # ----------------------------------------------------------
    def procesar_pago(self):
        """Simula el proceso de pago y guarda el resultado."""
        if not self.validar_metodo_pago():
            return

        print("Procesando pago...")
        time.sleep(1.5)

        exito = random.choice([True, False])  # Simulación aleatoria
        if exito:
            self.estado = "aprobado"
            print(f"Pago #{self.id_pago} aprobado por un monto de ${self.monto:,.2f}.")
        else:
            self.estado = "fallido"
            print("El pago no pudo completarse correctamente.")

        # Guardar en archivo JSON
        self.guardar_json()

    # ----------------------------------------------------------
    # Guardar información del pago
    # ----------------------------------------------------------
    def guardar_json(self, ruta_archivo="data/pagos.json"):
        """Guarda los pagos en un archivo JSON (se crea si no existe)."""
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

        data = []
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        data.append({
            "ID Pago": self.id_pago,
            "Monto": self.monto,
            "Método": self.metodo_pago,
            "Estado": self.estado
        })

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Información del pago #{self.id_pago} guardada en '{ruta_archivo}'.")

    # ----------------------------------------------------------
    # Representación en texto
    # ----------------------------------------------------------
    def __str__(self):
        return f"Pago #{self.id_pago} - {self.metodo_pago} - ${self.monto:,.2f} - Estado: {self.estado}"
