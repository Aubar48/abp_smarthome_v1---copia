# Diagrama de Clases - SmartHome (Evidencia 6 - Patrón DAO)

Este diagrama representa la arquitectura actual del sistema SmartHome con el patrón Data Access Object (DAO), mostrando la separación entre la capa de dominio, acceso a datos y servicios.

## Diagrama UML en Mermaid

```mermaid
classDiagram
    %% ===== CAPA DE DOMINIO =====
    class Usuario {
        -int id_usuario
        -string email
        -string nombre
        -string contraseña
        -string rol
        -datetime fecha_registro
        -bool activo
        +__init__(id, email, nombre, contraseña, rol, fecha_registro, activo)
        +__str__() string
    }

    class Vivienda {
        -int id_vivienda
        -string nombre_vivienda
        -string direccion
        -int id_administrador
        -bool activa
        +__init__(id, nombre, direccion, id_admin, activa)
        +__str__() string
    }

    class Dispositivo {
        -int id_dispositivo
        -string nombre_dispositivo
        -string tipo
        -string estado
        -string ubicacion
        -int id_vivienda
        +__init__(id, nombre, tipo, estado, ubicacion, id_vivienda)
        +__str__() string
    }

    class EventoDispositivo {
        -int id_evento
        -int id_dispositivo
        -int id_usuario
        -string tipo_evento
        -datetime fecha_hora
        -string detalle
        +__init__(id, id_disp, id_user, tipo, fecha, detalle)
        +__str__() string
    }

    %% ===== INTERFACES DAO =====
    class IUsuarioDAO {
        <<interface>>
        +crear(usuario)* int
        +obtener_todos()* list~Usuario~
        +obtener_por_id(id)* Usuario
        +actualizar(usuario)* void
        +eliminar(id)* void
    }

    class IViviendaDAO {
        <<interface>>
        +crear(vivienda)* int
        +obtener_todos()* list~Vivienda~
        +obtener_por_id(id)* Vivienda
        +actualizar(vivienda)* void
        +eliminar(id)* void
    }

    class IDispositivoDAO {
        <<interface>>
        +crear(dispositivo)* int
        +obtener_todos()* list~Dispositivo~
        +obtener_por_id(id)* Dispositivo
        +actualizar(dispositivo)* void
        +eliminar(id)* void
    }

    class IEventoDispositivoDAO {
        <<interface>>
        +crear(evento)* int
        +obtener_todos()* list~EventoDispositivo~
        +obtener_por_id(id)* EventoDispositivo
        +eliminar(id)* void
    }

    %% ===== IMPLEMENTACIONES DAO =====
    class UsuarioDAO {
        +crear(usuario) int
        +obtener_todos() list~Usuario~
        +obtener_por_id(id) Usuario
        +obtener_por_email(email) Usuario
        +actualizar(usuario) void
        +eliminar(id) void
    }

    class ViviendaDAO {
        +crear(vivienda) int
        +obtener_todos() list~Vivienda~
        +obtener_por_id(id) Vivienda
        +obtener_por_usuario(id_usuario) list~Vivienda~
        +actualizar(vivienda) void
        +eliminar(id) void
        +asignar_usuario(id_usuario, id_vivienda) void
    }

    class DispositivoDAO {
        +crear(dispositivo) int
        +obtener_todos() list~Dispositivo~
        +obtener_por_id(id) Dispositivo
        +obtener_por_vivienda(id_vivienda) list~Dispositivo~
        +actualizar(dispositivo) void
        +eliminar(id) void
    }

    class EventoDispositivoDAO {
        +crear(evento) int
        +obtener_todos() list~EventoDispositivo~
        +obtener_por_id(id) EventoDispositivo
        +obtener_por_dispositivo_id(id_disp) list~EventoDispositivo~
        +eliminar(id) void
    }

    %% ===== CAPA DE SERVICIOS =====
    class UsuarioService {
        -UsuarioDAO usuario_dao
        +__init__()
        +login(email, contraseña) Usuario
        +registrar_usuario(nombre, email, contraseña, rol) int
    }

    class ViviendaService {
        -ViviendaDAO vivienda_dao
        -DispositivoDAO dispositivo_dao
        +__init__()
        +crear_vivienda(nombre, direccion, id_admin) int
        +asignar_usuario_a_vivienda(id_usuario, id_vivienda) void
        +obtener_viviendas_por_usuario(id_usuario) list~Vivienda~
        +agregar_dispositivo_a_vivienda(nombre, tipo, ubicacion, id_vivienda) void
        +obtener_dispositivos_por_vivienda(id_vivienda) list~Dispositivo~
    }

    %% ===== CONEXIÓN A BASE DE DATOS =====
    class DBConnection {
        <<utility>>
        +DB_CONFIG dict
        +obtener_conexion() Connection
    }

    %% ===== RELACIONES =====
    
    %% Interfaces implementadas por DAOs
    IUsuarioDAO <|.. UsuarioDAO : implements
    IViviendaDAO <|.. ViviendaDAO : implements
    IDispositivoDAO <|.. DispositivoDAO : implements
    IEventoDispositivoDAO <|.. EventoDispositivoDAO : implements

    %% DAOs usan DBConnection
    UsuarioDAO ..> DBConnection : uses
    ViviendaDAO ..> DBConnection : uses
    DispositivoDAO ..> DBConnection : uses
    EventoDispositivoDAO ..> DBConnection : uses

    %% DAOs trabajan con entidades de dominio
    UsuarioDAO ..> Usuario : creates/returns
    ViviendaDAO ..> Vivienda : creates/returns
    DispositivoDAO ..> Dispositivo : creates/returns
    EventoDispositivoDAO ..> EventoDispositivo : creates/returns

    %% Services usan DAOs
    UsuarioService o-- UsuarioDAO : has-a
    ViviendaService o-- ViviendaDAO : has-a
    ViviendaService o-- DispositivoDAO : has-a

    %% Relaciones de negocio
    Vivienda "1" --> "1" Usuario : administrada por
    Dispositivo "n" --> "1" Vivienda : pertenece a
    EventoDispositivo "n" --> "1" Dispositivo : registra
    EventoDispositivo "n" --> "1" Usuario : generado por
    Usuario "n" --> "n" Vivienda : accede a
```

## Descripción de las Capas

### 1. Capa de Dominio (Entidades)
Las clases de dominio representan las entidades del negocio:
- **Usuario**: Representa a un usuario del sistema con credenciales y rol.
- **Vivienda**: Representa una casa inteligente con su información y administrador.
- **Dispositivo**: Representa un dispositivo IoT (luz, termostato, cámara, etc.).
- **EventoDispositivo**: Registra las acciones realizadas sobre los dispositivos.

### 2. Capa de Acceso a Datos (DAO)

#### Interfaces DAO
Definen los contratos que deben cumplir las implementaciones:
- **IUsuarioDAO**, **IViviendaDAO**, **IDispositivoDAO**, **IEventoDispositivoDAO**
- Métodos estándar: `crear()`, `obtener_todos()`, `obtener_por_id()`, `actualizar()`, `eliminar()`

#### Implementaciones DAO
Clases concretas que implementan las interfaces y manejan las operaciones CRUD:
- **UsuarioDAO**: Gestión de usuarios en la base de datos.
- **ViviendaDAO**: Gestión de viviendas y relación con usuarios.
- **DispositivoDAO**: Gestión de dispositivos asociados a viviendas.
- **EventoDispositivoDAO**: Registro de eventos en la base de datos.

### 3. Capa de Servicios (Lógica de Negocio)
Orquesta las operaciones de negocio usando los DAOs:
- **UsuarioService**: Maneja el login y registro de usuarios.
- **ViviendaService**: Coordina la creación de viviendas, asignación de usuarios y gestión de dispositivos.

### 4. Conexión a Base de Datos
- **DBConnection**: Utilidad que provee conexiones a MySQL.

## Patrones de Diseño Aplicados

1. **DAO (Data Access Object)**: Separa la lógica de persistencia de la lógica de negocio.
2. **Interface/Abstract Class**: Define contratos para las implementaciones DAO.
3. **Service Layer**: Encapsula la lógica de negocio y coordina operaciones.
4. **Dependency Injection**: Los servicios reciben instancias de DAOs.

## Ventajas de esta Arquitectura

✅ **Separación de responsabilidades**: Cada capa tiene un propósito específico.  
✅ **Testabilidad**: Las interfaces permiten crear mocks para pruebas.  
✅ **Mantenibilidad**: Los cambios en la BD no afectan la lógica de negocio.  
✅ **Escalabilidad**: Fácil agregar nuevas entidades o servicios.  
✅ **Reutilización**: Los DAOs pueden usarse en múltiples servicios.
