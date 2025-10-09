
# Smart Home : Sistema de Gestión de Dispositivos Inteligentes.

Este proyecto forma parte de la primera entrega del ABP del módulo Programador para la Tecnicatura en Desarrollo de Software. 
Consiste en un programa desarrollado en Python para gestionar dispositivos de iluminación del hogar y aplicar automatizaciones.

Mediante consola permite realizar operaciones CRUD sobre los dispositivos y activar automatizaciones predefinidas.



## Funciones
- _Listar_ todos los dispositivos existentes.
- _Buscar_ dispositivo por nombre.
- _Agregar_ dispositivo.
- _Editar_ dispositivo.
- _Eliminar_ dispositivos por nombre.
- _Ver_ automatizaciones.
- _Activar_ automatizaciones.
- _Ver_ datos personales.
- _Consultar_ automatizaciones activas.
- _Iniciar_ sesión
- _Agregar_ Usuario 
- 

## Automatización
Para esta primera entrega del ABP, desarrollamos una automatización 
llamada modo "Noche", cuya función es encender automáticamente las 
luces exteriores. 
Actualmente, la lógica se basa en verificar dos condiciones: que el dispositivo 
sea del tipo "luz exterior" y que su estado actual sea "apagado". Si ambas 
se cumplen, el sistema cambia su estado a "encendido". En caso de que el 
dispositivo ya esté encendido o no sea del tipo indicado, no se realiza 
ninguna modificación.


## Cómo ejecutar el proyecto

Clonar el repositorio

```bash
  git clone https://github.com/danaemeneses/abp_smarthome
```

Ingresar a la carpeta 'Programacion'
```bash
  cd .\Programacion\
```

Correr el archivo main
```bash
  python main.py
```
    
## Autores - Tec. en Desarrollo de Software - ISPC

- [@adriel1364](https://github.com/adriel1364)
- [@eliiconcep](https://github.com/eliiconcep)
- [@rooyar](https://github.com/rooyar)
- [@LeandroUlloque](https://github.com/LeandroUlloque)

