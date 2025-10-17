from Cliente import Cliente
from Habitaciones import Habitacion
from Reservacion import Reservacion
from Pagos import Pago
from datetime import datetime
import random

clientes = []
habitaciones = []
reservas = []


# --------------------------------------------------------------
# Función auxiliar para validar fechas
# --------------------------------------------------------------
def validar_fecha(fecha: str) -> bool:
    """Verifica que la fecha esté en formato YYYY-MM-DD y sea una fecha válida."""
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# --------------------------------------------------------------
# Menú principal
# --------------------------------------------------------------
def mostrar_menu():
    print("\n" + "=" * 40)
    print("        HOTEL SENA - MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Registrar cliente")
    print("2. Registrar habitación")
    print("3. Crear reservación")
    print("4. Ver clientes")
    print("5. Ver habitaciones")
    print("6. Ver reservaciones")
    print("7. Salir")
    print("8. Procesar pago de una reservación")
    print("=" * 40)


# --------------------------------------------------------------
# Registrar nuevo cliente
# --------------------------------------------------------------
def registrar_cliente():
    print("\n--- Registrar nuevo cliente ---")
    nombre = input("Nombre del cliente: ").strip()
    correo = input("Correo electrónico: ").strip()
    telefono = input("Teléfono: ").strip()

    try:
        cliente = Cliente(len(clientes) + 1, nombre, correo, telefono)
        clientes.append(cliente)
        print(f"Cliente {cliente.nombre} registrado con éxito.")
    except ValueError as e:
        print(f"Error: {e}")


# --------------------------------------------------------------
# Registrar nueva habitación
# --------------------------------------------------------------
def registrar_habitacion():
    print("\n--- Registrar nueva habitación ---")
    try:
        id_hab = len(habitaciones) + 1
        tipo = input("Tipo de habitación (Sencilla, Doble, Suite): ").strip().capitalize()
        precio = float(input("Precio por noche: "))
        habitacion = Habitacion(id_habitacion=id_hab, tipo=tipo, precio=precio)
        habitaciones.append(habitacion)
        print(f"Habitación {habitacion.tipo} registrada correctamente.")
    except ValueError:
        print("Error: El precio debe ser un número válido.")


# --------------------------------------------------------------
# Crear nueva reservación
# --------------------------------------------------------------
def crear_reservacion():
    print("\n--- Crear nueva reservación ---")

    if not clientes or not habitaciones:
        print("Debes tener al menos un cliente y una habitación registrada.")
        return

    try:
        id_reserva = len(reservas) + 1

        # Seleccionar cliente
        print("\nClientes disponibles:")
        for c in clientes:
            print(f"{c.id_cliente}. {c.nombre}")
        id_cliente = int(input("Seleccione el ID del cliente: "))
        cliente = next((c for c in clientes if c.id_cliente == id_cliente), None)
        if not cliente:
            print("Cliente no encontrado.")
            return

        # Seleccionar habitación disponible
        print("\nHabitaciones disponibles:")
        disponibles = [h for h in habitaciones if h.verificar_disponibilidad()]
        if not disponibles:
            print("No hay habitaciones disponibles.")
            return
        for h in disponibles:
            print(f"{h.id_habitacion}. {h.tipo} - ${h.precio:,.2f} - {h.estado}")
        id_hab = int(input("Seleccione el ID de la habitación: "))
        habitacion = next((h for h in habitaciones if h.id_habitacion == id_hab), None)
        if not habitacion:
            print("Habitación no encontrada.")
            return

        # Validar fechas de ingreso y salida
        fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ").strip()
        while not validar_fecha(fecha_ingreso):
            print("Formato o valor de fecha inválido. Ejemplo correcto: 2025-10-02")
            fecha_ingreso = input("Ingrese nuevamente la fecha de ingreso (YYYY-MM-DD): ").strip()

        fecha_salida = input("Fecha de salida (YYYY-MM-DD): ").strip()
        while not validar_fecha(fecha_salida):
            print("Formato o valor de fecha inválido. Ejemplo correcto: 2025-10-10")
            fecha_salida = input("Ingrese nuevamente la fecha de salida (YYYY-MM-DD): ").strip()

        # Verificar que la salida sea posterior al ingreso
        ingreso_dt = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        salida_dt = datetime.strptime(fecha_salida, "%Y-%m-%d")
        if salida_dt <= ingreso_dt:
            print("Error: la fecha de salida debe ser posterior a la fecha de ingreso.")
            return

        # Crear reservación
        reserva = Reservacion(
            id_reserva=id_reserva,
            cliente=cliente,
            habitacion=habitacion,
            fecha_ingreso=fecha_ingreso,
            fecha_salida=fecha_salida,
            precio=habitacion.precio
        )

        reservas.append(reserva)
        cliente.registrar_reserva(reserva.to_dict())
        print("Reservación creada correctamente.")
        reserva.mostrar_en_consola()
        reserva.guardar_json()

    except ValueError as e:
        print(f"Error de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error al crear la reservación: {e}")


# --------------------------------------------------------------
# Procesar pago de una reservación
# --------------------------------------------------------------
def procesar_pago_reservacion():
    print("\n--- Procesar pago de una reservación ---")

    if not reservas:
        print("No hay reservaciones registradas.")
        return

    # Mostrar reservas activas
    activas = [r for r in reservas if r.estado == "activa"]
    if not activas:
        print("No hay reservaciones activas para pagar.")
        return

    for r in activas:
        total = r.calcular_precio_total()
        print(f"ID: {r.id_reserva} | Cliente: {r.cliente.nombre} | Total: ${total:,.2f} | Habitación: {r.habitacion.tipo}")

    try:
        id_r = int(input("Seleccione el ID de la reservación para pagar: "))
        reserva = next((r for r in activas if r.id_reserva == id_r), None)
        if not reserva:
            print("Reservación no encontrada o no activa.")
            return

        metodo = input("Método de pago (tarjeta, nequi, daviplata, paypal): ").strip().lower()
        monto = reserva.calcular_precio_total()
        pago = Pago(id_pago=random.randint(1000, 9999), monto=monto, metodo_pago=metodo)
        pago.procesar_pago()

    except Exception as e:
        print(f"Ocurrió un error al procesar el pago: {e}")


# --------------------------------------------------------------
# Ver clientes registrados
# --------------------------------------------------------------
def ver_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    for c in clientes:
        c.mostrar_en_consola()


# --------------------------------------------------------------
# Ver habitaciones registradas
# --------------------------------------------------------------
def ver_habitaciones():
    if not habitaciones:
        print("No hay habitaciones registradas.")
        return
    for h in habitaciones:
        h.mostrar_en_consola()


# --------------------------------------------------------------
# Ver todas las reservaciones
# --------------------------------------------------------------
def ver_reservaciones():
    if not reservas:
        print("No hay reservaciones registradas.")
        return
    for r in reservas:
        r.mostrar_en_consola()


# --------------------------------------------------------------
# Bucle principal
# --------------------------------------------------------------
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            registrar_habitacion()
        elif opcion == "3":
            crear_reservacion()
        elif opcion == "4":
            ver_clientes()
        elif opcion == "5":
            ver_habitaciones()
        elif opcion == "6":
            ver_reservaciones()
        elif opcion == "8":
            procesar_pago_reservacion()
        elif opcion == "7":
            print("Gracias por usar el sistema del Hotel Sena. Hasta pronto.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
