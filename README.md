# Smart Home: Sistema de Gestión de Dispositivos Inteligentes

Este proyecto, desarrollado como parte de la Tecnicatura en Desarrollo de Software en ISPC, consiste en un sistema de gestión para una casa inteligente (Smart Home). Permite administrar usuarios, dispositivos, y automatizaciones, evolucionando desde un enfoque procedural hasta una arquitectura orientada a objetos con persistencia de datos.

## Descripción del Proyecto

El sistema "Smart Home" está diseñado para controlar y monitorear dispositivos inteligentes en una vivienda. Las funcionalidades principales incluyen:

-   **Gestión de Usuarios:** Alta, baja y modificación de usuarios del sistema.
-   **Control de Dispositivos:** Agregar, configurar y monitorear dispositivos como luces, termostatos, cámaras, etc.
-   **Automatización:** Crear reglas y rutinas que se ejecutan automáticamente bajo ciertas condiciones (ej. "apagar todas las luces a las 11 PM").
-   **Registro de Eventos:** Guardar un historial de las interacciones con los dispositivos.

## Evolución del Proyecto

El proyecto se ha desarrollado en varias etapas o "Evidencias", cada una construida sobre la anterior para incorporar nuevos conceptos de programación.

### Evidencia 3: Programación Estructurada

En esta primera fase, el sistema se desarrolló utilizando un paradigma de **programación procedural**. La lógica se organiza en funciones y módulos de Python.

-   `usuarios.py`: Funciones para la gestión de usuarios.
-   `dispositivos.py`: Funciones para el control de dispositivos.
-   `automatizacion.py`: Lógica para las automatizaciones.
-   `registro.py`: Manejo del historial de eventos.
-   `main.py`: Punto de entrada principal de la aplicación.

### Evidencia 5: Programación Orientada a Objetos (POO) y TDD

La segunda etapa refactoriza el código para aplicar el paradigma de **Programación Orientada a Objetos (POO)**. Cada entidad del sistema (Usuario, Dispositivo, etc.) se convierte en una clase, encapsulando sus datos y comportamientos.

Además, se introduce el **Desarrollo Guiado por Pruebas (TDD)** para asegurar la calidad y el correcto funcionamiento de cada clase.

-   `clase_usuario.py`, `clase_dispositivo.py`, etc.: Clases que modelan las entidades del sistema.
-   `prueba_usuario.py`, `prueba_dispositivo.py`, etc.: Pruebas unitarias para cada clase.
-   `ejecutar_pruebas_tdd.py`: Script para correr todas las pruebas.

### Evidencia 6: Patrón de Acceso a Datos (DAO)

En la última fase, se implementa el patrón **Data Access Object (DAO)** para separar la lógica de negocio de la lógica de acceso a datos. Esto permite que la aplicación interactúe con una base de datos (SQLite en este caso) de manera ordenada y escalable.

-   **`dominio/`**: Contiene las clases del negocio (Usuario, Vivienda, etc.).
-   **`dao/`**: Contiene los objetos DAO (`usuario_dao.py`, `vivienda_dao.py`) responsables de las operaciones CRUD (Crear, Leer, Actualizar, Borrar) en la base de datos.
-   **`services/`**: Coordina la lógica de negocio, utilizando los DAO para la persistencia.
-   **`conn/`**: Gestiona la conexión con la base de datos `smarthome.db`.
-   **`main.py`**: Punto de entrada que integra todas las capas.

## Cómo Ejecutar el Proyecto

Dependiendo de la evidencia que se quiera probar, se debe navegar a la carpeta correspondiente y ejecutar el archivo principal de Python.

### Para Evidencia 6 (versión más reciente):

1.  Asegúrate de tener Python instalado.
2.  Abre una terminal en la carpeta `SmartHome-DAO/`.
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4.  Ejecuta la aplicación:
    ```bash
    python main.py
    ```
