# Asistente General de Analistas de Ciberseguridad (A.G.A.C)

[cite_start]Este proyecto [cite: 1] [cite_start]ofrece respuestas a preguntas comunes para analistas y estudiantes en el campo en constante expansión de la ciberseguridad. [cite: 1]

[cite_start]El objetivo principal de este asistente [cite: 2] [cite_start]es facilitar el reconocimiento de medidas de mitigación contra vulnerabilidades y la comprensión de comandos esenciales para análisis forenses. [cite: 2] [cite_start]Resuelve la incertidumbre que puede surgir durante el estudio o en la labor diaria de un analista de ciberseguridad. [cite: 3] [cite_start]Las respuestas están formateadas con líneas separadoras para una lectura más sencilla y clara. [cite: 4]

## [cite_start]Características Principales [cite: 5]

* [cite_start]Orientación sobre mitigación de riesgos y respuesta a incidentes. [cite: 5]
* [cite_start]Información detallada sobre comandos útiles para verificación de seguridad. [cite: 5]

## Requisitos

* [cite_start]Python 3 (cualquier versión reciente debería funcionar). [cite: 5]

## [cite_start]Estructura del Proyecto [cite: 6]

[cite_start]El proyecto está dividido actualmente en dos carpetas principales: `Vulnerabilidades` y `Comandos`. [cite: 6]

* [cite_start]La carpeta `Vulnerabilidades` contiene subcarpetas que albergan los módulos de las distintas vulnerabilidades explicadas en el programa. [cite: 6]
* [cite_start]La carpeta `Comandos` cumple una función similar, alojando los módulos de los comandos explorados en el programa. [cite: 6]

## [cite_start]Uso [cite: 7]

[cite_start]Al iniciar el programa, se presentará una interfaz que explica su propósito y los temas disponibles para explorar. [cite: 7] [cite_start]Para navegar, se utilizan los números del teclado. [cite: 7] [cite_start]Simplemente lee y sigue las instrucciones en pantalla, que te guiarán sobre cómo usar los números para desplazarte entre las interfaces. [cite: 8]

[cite_start]Por ejemplo, para acceder a la sección de **Comandos de Verificación de Seguridad**, debes presionar el número correspondiente (1, 2, etc.) que se muestre en la interfaz. [cite: 9] [cite_start]La lógica de selección de opciones en el código fuente se maneja de la siguiente manera: 

```python
tema_escogido = int(input("Respuesta:"))
            if tema_escogido == 1:
                seccion_vulnerabilidades()
            elif tema_escogido == 2:
                seccion_comandos()
