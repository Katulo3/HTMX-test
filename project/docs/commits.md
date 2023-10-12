# Convención para commits

1. Se usará una _palabra clave_ en inglés, un espacio, y luego la explicación en español (salvo que se trate de un nombre de ruta o función), sin terminar en punto.
2. Cuando se haga referencia a un archivo se hará, por ej. `apps/cliente/views.py`
3. Cuando la ruta es larga se puede hacer lo siguiente: `.../templates/cliente/base.html`
4. Cuando se haga referencia a una función, clase o variable, usar el signo mayor: `apps.cliente.views.py > index`

- **Initial commit**: Primer commit luego de haber creado el entorno virtual, .gitignore, y haber configurado pyproject.toml. Ejemplo:

    `Initial commit`

## Trabajo sobre el código

- **Add** Nuevos archivos. Si el archivo es código que en sí mismo es una unidad funcional, corresponde Feature y no NEW. Este último es para señalar la creación de archivos que no son una característica en sí mismos para el proyecto. Puede ser documentación, imágenes, o código que aún no está siendo trabajado. Ejemplo:
  
    `Add imágenes predeterminadas que servirán de avatares para los usuarios`

- **Update** No se trata de arreglos de bugs etiquetados como tal. No se trata de refactorización ni de una nueva característica.

    `Update vistas basadas en clases que estaban comentadas`

- **Remove** Se quitan archivos.

    `Remove carpeta tal`

- **Wip:** (work in progress). Sirve para guardar un trabajo para luego continuarlo en otro momento

    `Wip: falta revisar si tal cosa funciona`
  
- **Feature** Nueva característica (conjunto de archivos de código que son dependientes entre sí, o un nuevo archivo que realmente sea una parte del sistema). Debe ir seguido de dos puntos y luego la explicación en mayúsculas.

    `Feature formulario de la app Clientes > urls, views y forms`

- **Release** La nueva versión etiquetada.

    `Release 0.2.0`

## Problemas y soluciones en el código

- **Test** Prueba unitaria que ha quedado funcional.

    `Test apps/cliente/models.py`
  
- **Bug** Cuando hay un commit en el que se conoce que hay un problema que arreglar.

    `Bug entro a la url me da tal error`

- **Fix** Cuando se arregló algún problema en el código.

    `Fix cuando se entraba a la url tal, daba tal error`

## Documentación

- **Doc** Se crea documentación dentro del código. La explicación del código: como una importación absoluta, ya que los docstring documentan objetos Python

    `Doc apps/cliente/models.py > Validaciones`

- **Typo** Corrección de ortografía o de gramática de la documentación fuera o dentro del código.

    `Typo docs/README.md`

    `Typo apps/cliente.py > Validaciones`

## Legibilidad

- **Format** Mejoras en la indentación, estructura. No cambia el código.

    `Format: .../templates/cliente.html`

- **Refactor** Mejoras en el código en cuanto legibilidad, técnicas, etc. No son correcciones de errores ni se agregan funcionalidades a la aplicación.

    `Refactor apps/cliente/views.py`

## Dependencias

- **Install** Instalación de una dependencia del proyecto

    `Install Django`

- **Uninstall** Desinstalación de una dependencia del proyecto

    `Uninstall Django`

- **Upgrade** Actualización de una dependencia del proyecto

    `Upgrade Django: 5`
