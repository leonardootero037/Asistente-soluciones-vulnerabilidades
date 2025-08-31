#Escrito por: Leonardo Otero
#16/07/2025
#Version: 2

print ("Bienvenido")
print ("Este es un modelo sencillo de un asistente de sugerencias para soluciones de vulnerabilidades")
print ("Escriba la vulnerabilidad para la que necesita soluciones")

#Definiendo respuestas a las distintas vulnerabilidades posibles

respuestas_vulnerabilidad_control_acceso = ["Implementar sistema de autenticación", "Implementar sistema de privilegios según nivel de usuario", "Implementar validación de funcionalidades del lado del servidor solamente"]
respuestas_vulnerabilidad_virus = ["Descargar e instalar los parches necesarios para los SO y las aplicaciones", "Actualizar software anti-virus", "Actualizar SO", "Concientizar sobre el pishing y enlaces maliciosos", "Activar el firewall"]
respuestas_vulnerabilidad_ransomware = ["Crear respaldos de los archivos en servidores basados en la nube", "Adaptar los servidores fisicos a la nube", "Crear e implementar un plan de respuesta ante incidentes"]
respuestas_vulnerabilidad_fisica = ["Contratar personal de seguridad", "Implementar sistema de acceso fisico a las instalaciones mediante tarjetas de acceso", "Instalar o mejorar las barreras de seguridad (muros, cercas, etc.)"]

#Definiendo explicaciones detalladas de cada solución de vulnerabilidad de control de acceso

explicacion_detallada_sistema_autenticacion = """Escriba politicas donde se defina los distintos rangos de usuario, el privilegio de los usuarios, requisitos para el registro e inicio de sesión, las consecuencias de ingresar la contraseña incorrecta, y las sanciones o consecuencias de no seguir los procedimientos requeridos. También escriba una politica sobre los requerimientos obligatorios de las contraseñas.
Use un sistema de autenticacion preexistente, como Auth0 u Okta, o cree su propio sistema de autenticación usando los framework disponibles para los distintos lenguajes de programación, como Django para Python, o ASP.NET Cora para C++.
Cree un salt (cadena aleatoria) para cada contraseña. Cifre las credenciales de los usuarios usando sistemas preexistentes criptograficos para crear hashes para contraseñas. Almacene el salt y hash de la contraseña en la base de datos de la empresa.
En el sistema de autenticación, la contraseña ingresada sera cifrada y su hash se comparara con los almacenados en la base de datos, si coincide, se accedera al sistema y recuraos disponibles para el rango del usuario."""
explicacion_detallada_sistema_privilegios = """Identifique los distintos rangos que existen en la organización, y con esto, comience a ir definiendo los roles que pueden llegar a tener los usuarios, y despues escriba scripts donde se defina cada rol, y a estos roles se les asigne distintas funciones existentes en el sistema.
Implemente en su sistema actualizaciones en las que el esquema de los usuarios en la base de datos empresarial cambie para incluir el apartado: rol. Despues se ira asignando manualmente a cada usuario existente un rol, solo el rol más alto podra acceder a las funciones y recursos mas valiosos."""
explicacion_detallada_validacion_servidor = """Identifique cuales son las funciones más importantes y criticas posibles, e identifique que roles de usuario tienen acceso a ellas.
Escriba un script donde se verifique la identidad del usuario, y despues se verifique si su rol asignado le permite realizar la función solicitada.
Si el usuario esta autenticado, y su rol es el necesario, la función solicitada sera ejecutada"""


#Definiendo explicaciones detalladas de cada solución de vulnerabilidad de ataque de malware

explicacion_detallada_parches_so = """Dirijase a la pagina web oficial del sistema operativo o aplicación del dispositivo vulnerable.
A continuación, busque una sección que haga referencia a: parches de seguridad. Escoja su versión de sistema operativo
y descargue el parche de seguridad, y una vez descargado, instalelo en el sistema operativo, despues, reinicie el dispositivo."""
explicacion_detallada_actualizar_antivirus = """Abra la aplicación de antivirus instalada en el dispositivo vulnerable. A continuación, busque en la sección de configuración alguna pestaña que haga referencia
a: actualizaciones, estando dentro de esa pestaña, presione la opción para buscar actualizaciones, y una vez encontradas, el programa las instalara automaticamente."""
explicacion_detallada_actualizar_so = """Abra el menu principal de su sistema operativo, y en busque una opción llamada: configuración. Dentro de la ventana de configuración, busque una sección, apartado, u opción que haga referencia a: actualización.
Dentro de esta ventana, haga clic en la opción: buscar actualizaciones. Las actualizaciones que encuentre el sistema seran descargadas automaticamente."""
explicacion_detallada_concientizacion = """Organice una reunión en una de las salas libres de las instalaciones de la empresa, y con diapositivas y dinamicas, comience a concientizar sobre los riesgos de responder a correos electronicos extraños o
no reconocidos"""

#Definiendo explicaciones detalladas de cada solución de vulnerabilidad de ataque ransomware

explicacion_detallada_respaldo_archivos = """Busque en Internet el servicio de almacenamiento en la nube más conveniente para la empresa.
Verifique que este servicio posea alguna de las certificaciones de ciberseguridad más importantes. Verifique si el servicio ofrece cifrado de datos almacenados cuando estos estan en reposo. Verifique que el servicio se acople perfectamente a su infraestructura
Determine cuales datos seran respaldados, cuanto tiempo seran respaldados, y cada cuanto se hara un nuevo respaldo.
Escriba un programa que ejecute las anteriores tareas y proteja los datos de ser violados."""
explicacion_detallada_adaptar_servidores = """Identifique los sistemas, aplicaciones, archivos y datos más importantes a proteger en la empresa.
Haga una auditoria para determinar que modelo de servicio (IaaS, PaaS, SaaS), servicio (Microsoft Azure, Google Cloud Platform, etc.), y estrategia de migración (Rehost, Refactor, Repurchase, etc.) es más adecuado para los objetivos de la empresa y los software y sistemas identificados.
Una vez escogidos el modelo de servicio y estrategia de migración, estos deben de comenzar a implementarse, empezando por la preparación del modelo de servicio, seguido de la ejecución de la estrategia.
El servidor en la nube debe de ser puesto a prueba despues, y debe de ser monitoreado constantemente."""
explicacion_detallada_plan_respuesta_incidentes = """Contacte a la gerencia de la empresa y planteele la creación de un equipo de respuesta a incidentes. Si le responden positivamente, la gerencia comenzara a escribir una politica donde se detalle los procedimientos a ejecutar contra cada tipo de incidente y donde se detalla el inventario de los activos a proteger, y usted capacite a personal de TI asignado por la gerencia para responder a los incidentes.
Con ese personal asignado por la gerencia, forme el equipo de respuesta a incidentes. 
Implemente sistemas que detecten trafico inusual en la red, y alerten sobre esto. Haga respaldo de los archivos importantes de forma periodica en la nube, asegurese de que ninguno de los dispositivos de los empleados tenga acceso o se sincronice con estos respaldos. Segmente la red, y aisle las partes segmentadas para dificultar la propagación del ransomware.
Si se detecta el ransomware, desconectar de la red todos los dispositivos afectados.
Llamar al equipo de respuesta a incidentes para eliminar el ransomware.
Comenzar a restaurar los archivos con sus copias subidas a la nube"""

#Definiendo explicaciones detalladas de cada solución de vulnerabilidad fisica

explicacion_detallada_contratar_personal = """Pregunte a la gerencia si contratar personal de seguridad y capacitarlo, o contratar a una organización de seguridad para que esta otorge personal.
La cantidad de personal de seguridad debe de ser suficiente para cubrir el interior y exterior de las instalaciones de la empresa.
Asegurese de que el personal sea competente, capaz de cooperar con otras fuerzas del orden y la justicia, capaz de manejar evacuaciones, capaz de responder a ataques fisicos y robos, y sea responsable con la vigilancia de los activos.
Implemente un sistema de circuito cerrado de televisión (CCV), y ponga a cargo en esa area a personal capacitado y certificado. Este sistema ayudara a que la respuesta del personal de seguridad sea más rapida."""
explicacion_detallada_tarjetas_acceso = """Desarrolle o compre un software de gestión de acceso basado en tarjetas (ACS). Este software alertara sobre los intentos de acceso no autorizados. Registre en ese sistema basado en software todo el personal de la instalación, y establezca sus roles y permisos. Escoja la tecnologia de las tarjetas de acceso (RFID, NFC, etc.). Escoja lectores compatibles con el software ACS y la tecnologia de las tarjetas.
Identifique las puertas a areas que no necesitan personal no autorizado en ellas. Otorgue a cada empleado su tarjeta de acceso, y expliqueles como usarlas.
Instale en las puertas priorizadas el lector de tarjetas de acceso.
Revise periodicamente los permisos y roles de cada usuario, y cambielos cuando sea necesario."""
explicacion_detallada_barreras_seguridad = """En base al tipo de suelo, sitio al que se accesa desde alli, y plan para esa area, determine si se necesita instalar: cercas, muros, bolardos, o portones. Si resulta necesario instalar alguna de esas opciones, acompañe cada una con sistemas CCTV e IDS.
Si desea mejorar la seguridad que proporciona cada uno, puede hacer lo siguiente:
    - Cercas: aumentar la altura de estas, añadirle puas, o electrificarlas.
    - Muros: aumentar la altura de estos, y añadirle puas, o alambre electrificado.
    - Bolardos: comprar bolardos certificados en resistencia contra impacto de vehiculos.
    - Puertas de seguridad: implementar un control de acceso basado en tarjetas de acceso."""

#Definiendo función para ofrecer soluciones a las vulnerabilidades
#La función tomara como parametro el texto que se le otorgue

def respuesta_a_vulnerabilidad(vulnerabilidad):
    vulnerabilidad_1 = vulnerabilidad.lower()
    if "acceso" in vulnerabilidad_1 or "control" in vulnerabilidad_1:
        print ("Soluciones:")
        for solucion in respuestas_vulnerabilidad_control_acceso:
            print ("-", solucion, sep = " ")
            
        print ("¿Desea obtener una explicación detallada de alguna solución?")
        respuesta = str(input("si/no"))
        if respuesta == "si":
            print ("¿De cual solución desea obtener explicación?")
            respuesta = str(input("1/2/3?"))
            if respuesta == "1":
                print (explicacion_detallada_sistema_autenticacion)
            elif respuesta == "2":
                print (explicacion_detallada_sistema_privilegios)
            elif respuesta == "3":
                print (explicacion_detallada_validacion_servidor)
            else:
                print ("No hay explicación detallada disponible")
        else:
            print ("Ok")
   
    elif "malware" in vulnerabilidad_1 or "virus" in vulnerabilidad_1:
          print ("Soluciones:")
          for solucion in respuestas_vulnerabilidad_virus:
              print ("-", solucion, sep = " ")
         
          print ("¿Desea obtener una explicación detallada de alguna solución?")
          respuesta = str(input("si/no"))
          respuesta_1 = respuesta.lower()
          if respuesta_1 == "si":
             print ("¿De cual solución desea obtener explicación?")
             respuesta = str(input("1/2/3/4/5?"))
             if respuesta == "1":
                print (explicacion_detallada_parches_so)
             elif respuesta == "2":
                 print (explicacion_detallada_actualizar_antivirus)
             elif respuesta == "3":
                 print (explicacion_detallada_actualizar_so)
             elif respuesta == "4":
                 print (explicacion_detallada_concientizacion)
             else:
                 print ("No hay explicación detallada disponible")
          else:
              print ("Ok")
      
    elif "cifrado" in vulnerabilidad_1 or "ransomware" in vulnerabilidad_1:
         print ("Soluciones:")
         for solucion in respuestas_vulnerabilidad_ransomware:
             print ("-", solucion, sep = " ")
             
         print ("¿Desea obtener una explicaciób detallada de alguna solución?")
         respuesta = str(input("si/no"))
         respuesta_1 = respuesta.lower()
         if respuesta_1 == "si":
             print ("¿De cual solución desea obtener explicación?")
             respuesta = str(input("1/2/3/?"))
             if respuesta == "1":
                 print (explicacion_detallada_respaldo_archivos)
             elif respuesta == "2":
                 print (explicacion_detallada_adaptar_servidores)
             elif respuesta == "3":
                 print (explicacion_detallada_plan_respuesta_incidentes)
             else:
                 print ("No hay explicación detallada disponible")
         else:
             print ("Ok")
             
    elif "atacaron" in vulnerabilidad_1 or "entraron" in vulnerabilidad_1:
         print ("Soluciones:")
         for solucion in respuestas_vulnerabilidad_fisica:
             print ("-", solucion, sep = " ")
         
         print ("¿Quiere obtener explicación detallada de alguna solución?")
         respuesta = str(input("si/no"))
         respuesta_1 = respuesta.lower()
         if respuesta_1 == "si":
            print ("¿De cual solución desea obtener explicación?")
            respuesta = str(input("1/2/3?"))
            if respuesta == "1":
                print (explicacion_detallada_contratar_personal)
            elif respuesta == "2":
                print (explicacion_detallada_tarjetas_acceso)
            elif respuesta == "3":
                print (explicacion_detallada_barreras_seguridad)
            else:
                print ("No hay explicación detallada disponible")
         else:
             print ("Ok")
                
                         

#Iniciando bucle principal

while True:
    vulnerabilidad1 = str(input("Vulnerabilidad:"))
    respuesta_a_vulnerabilidad(vulnerabilidad1)
    
    #Iniciando bucle segundario
    
    while True:
        print ("Quiere ver soluciones para otra vulnerabilidad?")
        respuesta = str(input("si/no"))
        if respuesta == "si":
            break
        elif respuesta == "no":
            print ("Esta bien, pero nos avisa")
            exit()
        else:
            print ("?")         
