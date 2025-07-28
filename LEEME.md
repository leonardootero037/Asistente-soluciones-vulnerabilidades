# Asistente General de Analistas de Ciberseguridad (A.G.A.C)

Este proyecto ofrece respuestas a preguntas comunes para analistas y estudiantes en el campo en constante expansión de la ciberseguridad.

El objetivo principal de este asistente es facilitar el reconocimiento de medidas de mitigación contra vulnerabilidades y la comprensión de comandos esenciales para análisis forenses. Resuelve la incertidumbre que puede surgir durante el estudio o en la labor diaria de un analista de ciberseguridad. Las respuestas están formateadas con líneas separadoras para una lectura más sencilla y clara.

## Características Principales

* Orientación sobre mitigación de riesgos y respuesta a incidentes.
* Información detallada sobre comandos útiles para verificación de seguridad.

## Requisitos

* Python 3 (cualquier versión reciente).

## Estructura del Proyecto

El proyecto está dividido actualmente en dos carpetas principales: `Vulnerabilidades` y `Comandos`.

* La carpeta `Vulnerabilidades` contiene subcarpetas que albergan los módulos de las distintas vulnerabilidades exploradas en el programa. 
* La carpeta `Comandos` cumple una función similar, alojando los módulos de los comandos explicados y ejemplificados en el programa.

## Uso

Para poder iniciar el programa, primero este debe ser descomprimido con algún software especializado en archivos .zip.
Una vez descomprimido, al iniciar el programa, se presentará una interfaz que explica su propósito y los temas disponibles para explorar. Para navegar por las interfaces, se utilizan los números del teclado. Simplemente lea y siga las instrucciones en pantalla, que le guiarán sobre cómo usar los números para desplazarse entre las interfaces.

Por ejemplo, para acceder a la sección de **Comandos de Verificación de Seguridad**, debes presionar el número correspondiente (en este caso: 2) que se muestre en la interfaz. La lógica de selección de opciones en el código fuente se maneja de la siguiente manera: 

```python
tema_escogido = int(input("Respuesta:"))
            if tema_escogido == 1:
                seccion_vulnerabilidades()
            elif tema_escogido == 2:
                seccion_comandos()
