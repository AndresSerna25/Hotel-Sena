from cliente import Cliente
from Habitaciones import habitacion
from Reservacion import Reservacion

# ============================================
#  🏨  SISTEMA DE RESERVACIONES HOTEL SENA
#  Autor: Maicol Steven Rincón Sánchez
#  Contacto: msrincon678@gmail.com
# ============================================

def main():
    print("\n===============================")
    print("  🏨 BIENVENIDO AL HOTEL SENA")
    print("===============================\n")

    # Crear un cliente
    cliente1 = Cliente(
        1,
        "Maicol Steven Rincón Sánchez",
        "msrincon678@gmail.com",
        3134974294
    )

    # Crear una habitación disponible
    habitacion1 = habitacion(
        id_habitacion=10,
        tipo="Suite",
        precio=120000,
        estado="disponible"
    )

    # Crear una reservación (la habitación se marca como 'reservada')
    reserva1 = Reservacion(
        id_reserva=1,
        cliente=cliente1,
        habitacion=habitacion1,
        fecha_ingreso="2025-10-20",
        fecha_salida="2025-10-25",
        precio=habitacion1.precio
    )

    # Mostrar reservación en formato elegante
    reserva1.mostrar_en_consola()

    # Guardar la reservación como JSON
    reserva1.guardar_json()

    # Mostrar como diccionario (para pruebas o conexión futura con base de datos)
    info = reserva1.mostrar_reservacion()
    print("\nDiccionario de datos:\n", info)

    # Cancelar la reservación y volver a mostrar
    reserva1.cancelar()
    reserva1.mostrar_en_consola()

if __name__ == "__main__":
    main()
