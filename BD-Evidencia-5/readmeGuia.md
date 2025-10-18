# README - Ejecución de Scripts SQL en un DBMS Online

Este proyecto contiene dos tipos de scripts SQL:

- **DDL (Data Definition Language):** crean y definen la estructura de la base de datos (tablas, llaves primarias, etc.).
- **DML (Data Manipulation Language):** insertan, actualizan, eliminan o consultan datos en las tablas ya creadas.

## Requisitos

No es necesario instalar software en tu computadora.  
Se recomienda usar un **DBMS online**, como:

- [db-fiddle.com](https://db-fiddle.com/) (MySQL, PostgreSQL, SQL Server, SQLite, Oracle)
- [sqlfiddle.com](http://sqlfiddle.com/) (más limitado, pero simple)
- [OneCompiler](https://onecompiler.com/mysql) (rápido para MySQL)

## Ejecución Paso a Paso

1. **Abrir el DBMS online**  
   Ingresa a [db-fiddle.com](https://db-fiddle.com/).

2. **Seleccionar el motor de base de datos**  
   Por ejemplo: `MySQL 8.0` (o el que indique tu profesor/a).

3. **Ejecutar las consultas DDL**  
   - Copia el contenido del archivo `consultasDDL.sql`.
   - Pégalo en el editor de consultas del DBMS online.
   - Haz clic en **Run** para crear la estructura de la base de datos.

   

4. **Ejecutar las consultas DML**  
   - Una vez creadas las tablas, copia el contenido del archivo `consultasDML.sql`.
   - Pégalo en el editor y haz clic en **Run** para insertar, actualizar o consultar datos.


5. **Verificar resultados**  
   - Los datos insertados se mostrarán en la parte inferior de la página del DBMS online.
   - Si hay errores, asegúrate de haber ejecutado **primero el archivo DDL** y luego el **DML**.

## Archivos del proyecto

- `ddl.sql` → Contiene las instrucciones para crear las tablas y estructuras de la base de datos.
- `dml.sql` → Contiene las instrucciones para insertar, modificar, eliminar y consultar datos.

