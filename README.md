# Chatbot de Soporte Técnico Nivel 1

## Trabajo Integrador - Organización Empresarial

**Universidad Tecnológica Nacional (UTN)**
**Tecnicatura Universitaria en Programación a Distancia**

### Integrante

* Tomas Sopranzetti

---

## Descripción

Este proyecto consiste en la simulación de un proceso de soporte técnico de nivel 1 mediante un chatbot desarrollado en Python.

El sistema permite identificar usuarios, registrar incidencias, consultar una base de conocimientos y brindar soluciones automáticas. En caso de no encontrar una solución, genera un ticket para su posterior atención por parte de un técnico especializado.

---

## Tecnologías utilizadas

* Python 3
* Archivos CSV
* Máquina de Estados
* BPMN 2.0

---

## Estructura del proyecto

```text
tpi_oe.py
usuarios.csv
incidencias.csv
tickets.csv
README.md
```

### Archivos

**usuarios.csv**

* Almacena los usuarios registrados.

**incidencias.csv**

* Contiene la base de conocimientos utilizada por el chatbot.

**tickets.csv**

* Registra las incidencias que requieren derivación a soporte técnico.

**tpi_oe.py**

* Código principal del sistema.

---

## Funcionalidades

* Identificación de usuarios.
* Registro de incidencias.
* Consulta automática de soluciones.
* Generación de tickets.
* Visualización de tickets generados.
* Gestión de estados del proceso.
* Acceso para técnico especializado.
* Actualización del estado de tickets.

---

## Acceso Técnico

El sistema cuenta con un perfil de técnico especializado para la gestión de tickets generados por el chatbot.

### Credenciales

```text
Usuario: admin
Contraseña: 1234
```

### Funciones disponibles

* Visualizar tickets generados.
* Consultar el estado actual de los tickets.
* Modificar el estado de los tickets.

### Estados posibles

* Pendiente
* En Proceso
* Resuelto

Esta funcionalidad simula la participación del Técnico Especializado definida en el proceso TO-BE modelado mediante BPMN.

---

## Ejecución

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:

```bash
python tpi_oe.py
```

3. Seleccionar una opción del menú principal.

### Menú principal

```text
1. Realizar consulta
2. Acceso técnico
3. Ver tickets generados
4. Salir
```

---

## Flujo del proceso

1. El usuario inicia una consulta.
2. El chatbot identifica al usuario.
3. Se registra la incidencia.
4. Se consulta la base de conocimientos.
5. Si existe una solución, se muestra al usuario.
6. Si no existe, se genera un ticket de soporte.
7. El técnico puede consultar y actualizar el estado del ticket.
8. El proceso finaliza.

---

## Autor

Tomas Sopranzetti

Trabajo Práctico Integrador - Organización Empresarial - UTN
