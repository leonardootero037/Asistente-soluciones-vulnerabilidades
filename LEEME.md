# Asistente General de Analistas de Ciberseguridad (A.G.A.C)

Este proyecto pretende ayudar con problemas que pueden surgir a la hora del estudio de la ciberseguridad, como la falta de orientación.

El objetivo principal de este asistente es facilitar el reconocimiento y la comprensión de áreas clave de la ciberseguridad, como las medidas de mitigación contra vulnerabilidades y los comandos esenciales para análisis forenses. Ayudando de esta manera a orientar a los estudiantes, facilitar el reconocimiento de conceptos para los especialistas, e informar a los funcionarios de la empresa que no pertenezcan al área informática.
En el programa las respuestas están formateadas con líneas separadoras para una lectura más sencilla y clara.

## Características Principales

* Orientación sobre mitigación de vulnerabilidades.
* Información sobre comandos útiles para verificación de seguridad.

## Requisitos

* Python 3 (cualquier versión reciente).

## Estructura del Proyecto

El proyecto está dividido actualmente en tres carpetas principales: `Vulnerabilidades`, `Comandos`, y `Secciones`.

* La carpeta `Vulnerabilidades` contiene subcarpetas que albergan los módulos de las distintas vulnerabilidades exploradas en el programa. 
* La carpeta `Comandos` cumple una función similar, alojando los módulos de los comandos explicados y ejemplificados en el programa.
* La carpeta `Secciones` contiene dos subcarpetas, las cuales son `Glosario` y `Novedades`. `Glosario` contiene las definiciones de términos básicos usados en la ciberseguridad, y su objetivo es ayudar a los funcionarios no informáticos a tener una mayor comprensión sobre las áreas clave de este campo exploradas en el asistente. Y `Novedades`, valga la redundancia, contiene las novedades de la respectiva versión de A.G.A.C que este siendo usada.  

## Uso

Para poder iniciar el programa, primero este debe ser descomprimido con algún software especializado en archivos .zip o .rar.
Una vez descomprimido, al iniciar el programa, se presentará una interfaz que explica su propósito y los temas disponibles para explorar. Para navegar por las interfaces, se utilizan los números del teclado. Simplemente lea y siga las instrucciones en pantalla, que le guiarán sobre cómo usar los números para desplazarse entre las interfaces.

Por ejemplo, para acceder a la sección de **Comandos de Verificación de Seguridad**, debes presionar el número correspondiente (en este caso: 2) que se muestre en la interfaz. La lógica de selección de opciones en el código fuente se maneja de la siguiente manera: 

```python
 tema_escogido = int(input("Respuesta:"))
            print ("-" * 60)
            print ("")
            if tema_escogido == 1:
                print ("-" * 40)
                seccion_vulnerabilidades()
            elif tema_escogido == 2:
                print ("-" * 40)
                seccion_comandos()
            elif tema_escogido == 0:
                print ("-" * 40)
                seccion_tecnica()
