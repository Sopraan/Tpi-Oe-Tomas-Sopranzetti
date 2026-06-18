
import csv

# Estados utilizados por el chatbot para simular el ciclo de vida de una incidencia.
ESTADOS = {
    "INICIO": 0,
    "IDENTIFICACION": 1,
    "REGISTRO_INCIDENTE": 2,
    "BUSQUEDA_SOLUCION": 3,
    "RESUELTO": 4,
    "DERIVADO": 5,
    "FINALIZADO": 6
}

# Crea automáticamente el archivo de tickets si todavía no existe.
def inicializar_tickets():

    try:

        with open("tickets.csv", "x", encoding="utf-8", newline="") as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                "id_usuario",
                "nombre",
                "problema",
                "estado"
            ])

    except FileExistsError:
        pass

# Carga los usuarios registrados desde usuarios.csv
def cargar_usuarios():

    usuarios = {}

    try:

        with open("usuarios.csv", "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:
                usuarios[fila["id_usuario"]] = fila

    except FileNotFoundError:

        print("Error: no se encontró usuarios.csv")

    return usuarios

# Carga la base de conocimientos utilizada por el chatbot para resolver incidencias.
def cargar_incidencias():

    incidencias = []

    try:

        with open("incidencias.csv", "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:
                incidencias.append(fila)

    except FileNotFoundError:

        print("Error: no se encontró incidencias.csv")

    return incidencias


# Busca una solución asociada a la categoría ingresada por el usuario.
def buscar_solucion(problema, incidencias):

    for incidencia in incidencias:

        if problema.lower() == incidencia["categoria"].lower():
            return incidencia["solucion"]

    return None

# Genera un ticket cuando el chatbot no encuentra una solución automática.
def generar_ticket(usuario, problema):

    try:

        with open("tickets.csv", "a", encoding="utf-8", newline="") as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                usuario["id_usuario"],
                usuario["nombre"],
                problema,
                "Pendiente"
            ])

    except Exception as error:

        print("Error al generar ticket:", error)

# Simula la interacción principal entre el usuario y el chatbot de soporte técnico.

def chatbot():

    estado = ESTADOS["INICIO"]

    usuarios = cargar_usuarios()
    incidencias = cargar_incidencias()

    print("\n" + "=" * 50)
    print("CHATBOT DE SOPORTE TÉCNICO")
    print("=" * 50)
# Estado de identificación del usuario.
    estado = ESTADOS["IDENTIFICACION"]
    print("\n[Estado: IDENTIFICACION]")

    while True:

        id_usuario = input("Ingrese su ID de usuario: ").strip()

        if not id_usuario.isdigit():

            print("Error: el ID debe contener solo números.")
            continue

        if id_usuario not in usuarios:

            print("Usuario no encontrado.")
            continue

        usuario = usuarios[id_usuario]
        break

    print(f"\nBienvenido {usuario['nombre']}")
    print(f"Sector: {usuario['sector']}")
# Estado de registro de la incidencia.
    estado = ESTADOS["REGISTRO_INCIDENTE"]
    print("\n[Estado: REGISTRO_INCIDENTE]")

    while True:

        problema = input("\nDescriba el problema: ").strip()

        if problema == "":

            print("Debe ingresar una descripción.")
            continue

        if len(problema) < 3:

            print("La descripción es demasiado corta.")
            continue

        break
# Estado de búsqueda de solución.
    estado = ESTADOS["BUSQUEDA_SOLUCION"]
    print("\n[Estado: BUSQUEDA_SOLUCION]")

    solucion = buscar_solucion(problema, incidencias)

    if solucion:
# Solución encontrada en la base de conocimientos.
        estado = ESTADOS["RESUELTO"]
        print("\n[Estado: RESUELTO]")

        print("\nSOLUCIÓN ENCONTRADA")
        print(solucion)

        print("\nLa incidencia fue resuelta automáticamente.")

    else:
# El caso debe ser derivado a soporte técnico.
        estado = ESTADOS["DERIVADO"]
        print("\n[Estado: DERIVADO]")

        print("\nNo existe una solución registrada.")
        print("Se generará un ticket para soporte técnico.")

        generar_ticket(usuario, problema)

        print("Ticket generado correctamente.")

    estado = ESTADOS["FINALIZADO"]
    print("\n[Estado: FINALIZADO]")

    print("\nProceso finalizado.")
    print("Gracias por utilizar el sistema.")

def mostrar_tickets():

    try:

        with open("tickets.csv", "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            print("\n" + "=" * 70)
            print("TICKETS GENERADOS")
            print("=" * 70)

            for fila in lector:

                print(" | ".join(fila))

    except FileNotFoundError:

        print("\nNo existe el archivo de tickets.")

# Permite a un técnico actualizar el estado de un ticket existente.
def cambiar_estado_ticket():

    try:

        with open("tickets.csv", "r", encoding="utf-8") as archivo:

            tickets = list(csv.reader(archivo))

        if len(tickets) <= 1:

            print("\nNo hay tickets para gestionar.")
            return

        print("\nTICKETS DISPONIBLES")
        print("-" * 70)

        for i in range(1, len(tickets)):

            print(
                f"{i} - "
                f"{tickets[i][1]} | "
                f"{tickets[i][2]} | "
                f"{tickets[i][3]}"
            )

        while True:

            try:

                opcion = int(input("\nSeleccione un ticket: "))

                if 1 <= opcion < len(tickets):
                    break

                print("Ticket inexistente.")

            except ValueError:

                print("Debe ingresar un número.")

        print("\nEstados posibles")
        print("1. Pendiente")
        print("2. En Proceso")
        print("3. Resuelto")

        while True:

            nuevo_estado = input(
                "Seleccione nuevo estado: "
            ).strip()

            if nuevo_estado == "1":

                tickets[opcion][3] = "Pendiente"
                break

            elif nuevo_estado == "2":

                tickets[opcion][3] = "En Proceso"
                break

            elif nuevo_estado == "3":

                tickets[opcion][3] = "Resuelto"
                break

            else:

                print("Opción inválida.")

        with open(
            "tickets.csv",
            "w",
            encoding="utf-8",
            newline=""
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerows(tickets)

        print("\nEstado actualizado correctamente.")

    except FileNotFoundError:

        print("\nNo existe tickets.csv")

# Menú exclusivo para el técnico especializado.
def menu_tecnico():

    usuario = input("Usuario: ").strip()
    clave = input("Contraseña: ").strip()

    if usuario != "admin" or clave != "1234":

        print("\nCredenciales incorrectas.")
        return

    while True:

        print("\n" + "=" * 50)
        print("MENU TECNICO")
        print("=" * 50)
        print("1. Ver tickets")
        print("2. Cambiar estado de ticket")
        print("3. Volver")
        print("=" * 50)

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":

            mostrar_tickets()

        elif opcion == "2":

            cambiar_estado_ticket()

        elif opcion == "3":

            break

        else:

            print("Opción inválida.")

# Muestra las opciones principales del sistema.
def mostrar_menu():

    print("\n" + "=" * 50)
    print("SISTEMA DE SOPORTE TÉCNICO")
    print("=" * 50)
    print("1. Realizar consulta")
    print("2. Acceso técnico")
    print("3. Ver tickets generados")
    print("4. Salir")
    print("=" * 50)

# Controla la navegación entre los distintos menús.
def main():

    inicializar_tickets()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":

            chatbot()

        elif opcion == "2":

            menu_tecnico()

        elif opcion == "3":

            mostrar_tickets()

        elif opcion == "4":

            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado.")
            break

        else:

            print("\nOpción inválida.")
            print("Intente nuevamente.")


main()