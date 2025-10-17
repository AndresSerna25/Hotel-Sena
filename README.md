# 🏨 Sistema de Gestión Hotel Sena

Este proyecto es una aplicación de consola en **Python** que simula el sistema de administración de un hotel.  
Permite registrar clientes, habitaciones, crear reservaciones y procesar pagos, almacenando la información en archivos JSON.

---

## 📋 Características principales

- Registro de clientes con validaciones de nombre, correo y teléfono.  
- Registro de habitaciones con tipo, precio y estado (disponible, ocupada o reservada).  
- Creación de reservaciones con validación de fechas.  
- Cálculo automático del precio total de la estadía.  
- Procesamiento simulado de pagos (tarjeta, Nequi, Daviplata, PayPal).  
- Guardado automático de reservas y pagos en archivos `.json`.  
- Menú interactivo y fácil de usar desde la consola.

---

## 🧩 Estructura del proyecto

```text
HotelSena/
│
├── Cliente.py           # Clase Cliente (datos y validaciones)
├── Habitaciones.py      # Clase Habitacion (gestión de estado y precio)
├── Reservacion.py       # Clase Reservacion (manejo de fechas y precios)
├── pagos.py             # Clase Pago (procesamiento y registro de pagos)
├── hotel_main.py        # Programa principal (menú del sistema)
│
└── data/                # Carpeta generada automáticamente
    ├── reservas.json    # Historial de reservaciones
    └── pagos.json       # Historial de pagos
```

---

## ⚙️ Requisitos

- Python **3.8** o superior  
- No requiere librerías externas (usa solo módulos estándar de Python)

---

## ▶️ Ejecución del programa

1. Abre una terminal en la carpeta del proyecto.  
2. Ejecuta el archivo principal:

   ```bash
   python hotel_main.py
   ```

3. Usa el menú para interactuar con el sistema.

---

## 🧠 Opciones del menú

| Opción | Descripción |
|--------|--------------|
| **1** | Registrar nuevo cliente |
| **2** | Registrar nueva habitación |
| **3** | Crear nueva reservación |
| **4** | Ver todos los clientes |
| **5** | Ver todas las habitaciones |
| **6** | Ver todas las reservaciones |
| **7** | Salir del sistema |
| **8** | Procesar pago de una reservación |

---

## 💾 Archivos generados

Durante la ejecución, el sistema creará automáticamente una carpeta `data/` donde se guardarán los archivos:

- `reservas.json`: contiene todas las reservaciones creadas.  
- `pagos.json`: contiene todos los pagos procesados (aprobados o fallidos).

Ejemplo de `pagos.json`:

```json
[
    {
        "ID Pago": 1023,
        "Monto": 150000.0,
        "Método": "tarjeta",
        "Estado": "aprobado"
    }
]
```

---

## 👨‍💻 Equipo de desarrollo

**Autor principal:**  
- **Maicol Steven**

**Colaboradores:**  
- **Franklin Daniel Durán Santana** – [franklindanielduransantana@gmail.com](mailto:franklindanielduransantana@gmail.com)  
- **Andrés Felipe Serna Carrillo** – [andrescolab6@gmail.com](mailto:andrescolab6@gmail.com)  
- **Diego Alejandro Silva** – [diegoalejandrosilva12162005@gmail.com](mailto:diegoalejandrosilva12162005@gmail.com)

---

## 📜 Licencia

Este proyecto se distribuye con fines educativos y de libre uso.  
Puedes modificarlo y mejorarlo libremente.
