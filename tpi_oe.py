
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
