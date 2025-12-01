Sílabo revisado: Introducció a PHP + Estructures de dades + JSON
1. Información general

Nombre de la unidad: Introducció a PHP i manipulació de dades — bases per a interacció backend/frontend.

Tipo: Módulo introductorio / parte inicial de la asignatura mayor.

Carga estimada: 2–3 créditos ECTS (o equivalente en horas de docencia/prácticas).

Horas lectivas / prácticas: por ejemplo 8–10 h teóricas + 10–15 h prácticas / laboratorio.

Requisitos previos: Conocimientos de HTML y JavaScript (DOM, cliente web). No es necesario saber PHP.

Objetivo general: Que el estudiante aprenda la sintaxis básica de PHP, entienda cómo manipular datos en PHP mediante variables y arrays, y cómo convertir esas estructuras a JSON para interoperabilidad con cliente JS o almacenamiento.

2. Justificación y objetivo de la fase introductoria

En un entorno web moderno, es habitual tener un cliente (HTML + JS) que interactúa con un backend (PHP u otro lenguaje), intercambiando datos estructurados (JSON). Esta fase introductoria permite que estudiantes con base en cliente web se familiaricen con la parte servidor de forma sencilla, construyendo una base sólida sobre la que luego podrán añadir funcionalidades más complejas (recepción de correos, parseo, almacenamiento, APIs).

Objetivos específicos al final de esta unidad:

Entender qué es PHP, cómo se integra con HTML, y cómo configurar un entorno de desarrollo.

Saber declarar y usar variables en PHP; conocer los tipos básicos (strings, números, booleanos).

Conocer y usar arrays en PHP: arrays indexados, arrays asociativos, arrays multidimensionales. 
php.net
+2
IONOS
+2

Comprender e implementar la serialización y deserialización de estructuras PHP usando JSON (json_encode / json_decode). 
W3Schools
+2
phptutorial.net
+2

Preparar al alumno para intercambiar datos entre cliente JS y backend PHP, o para almacenar datos de forma estructurada en servidor.

3. Contenidos / Programa: temas de la unidad introductoria
Tema	Contenidos / subtemas
1. Qué es PHP — conceptos y entorno	Qué es PHP; servidor vs cliente; cómo incrustar PHP en HTML; configuración básica (instalación, servidor local o entorno de pruebas). Basado en manuales de inicio de PHP. 
Code Envato Tuts+
+1

2. Sintaxis básica de PHP — variables, operadores, salida	Variables en PHP (prefijo $, tipado dinámico), asignaciones, operadores básicos, mostrar contenido con echo/print, comentarios. 
freecodecamp.org
+1

3. Estructuras de control básicas (opcional en introducción)	Condicionales (if, else), bucles básicos (for, foreach, while) — útiles para recorrer arrays. 
freecodecamp.org
+1

4. Arrays en PHP: tipos y manipulación	Arrays — arrays indexados (listas), arrays asociativos (clave → valor), arrays multidimensionales. Crear, acceder, modificar, recorrer con bucles o foreach. 
php.net
+2
manualweb.net
+2

5. JSON en PHP: conversión entre PHP y JSON	Uso de json_encode() para transformar arrays/objetos PHP en JSON; uso de json_decode() para transformar JSON en estructuras PHP (array u objeto), con su correspondencia. 
W3Schools
+2
phptutorial.net
+2

6. Integración con cliente web (HTML + JS) / comunicación básica	Cómo generar JSON desde PHP y servirlo; desde cliente JS (fetch / AJAX) consumir ese JSON para integrar frontend y backend — puente entre conocimientos previos en JS y lo aprendido en PHP. (Intro conceptual; ejemplos simples)
7. Buenas prácticas iniciales: codificación, organización de código, estructura	Mantener código claro; uso de arrays asociativos/estructuras adecuadas para datos; pensar en JSON como interfaz de intercambio; breves notas sobre seguridad básica (aunque será desarrollada más adelante).
8. Ejercicios prácticos de consolidación	Varios ejercicios de práctica: scripts PHP simples que usen variables, arrays, luego conviertan arrays a JSON y lo muestren; pequeños “mini-proyectos” que combinen HTML + PHP + JSON para enviar/mostrar datos; preparación para fase avanzada.
4. Metodología docente

Clases teóricas + demostraciones en vivo: presentar sintaxis, explicar arrays, JSON, mostrar ejemplos.

Laboratorios / prácticas guiadas: los estudiantes codifican scripts PHP sencillos, prueban en entorno local, generan JSON, lo consumen desde JS.

Autoestudio / ejercicios entregables: listados de ejercicios para practicar variables, arrays, JSON; envío de tareas.

Reflexión sobre arquitectura cliente-servidor: explicar cuándo usar JSON, por qué estructurar datos, relación frontend-backend.

5. Evaluación (fase introductoria)

Debido a carácter introductorio, evaluación simple, por ejemplo:

Ejercicios prácticos (variables, arrays, JSON): 50 %

Pequeño mini-proyecto (HTML + PHP + JSON, cliente/servidor simple): 40 %

Participación / asistencia / entrega ejercicios: 10 %

También puede incluir una mini-prueba escrita o de código: preguntas cortas sobre sintaxis, estructuras de datos, diferencias entre arrays indexados y asociativos, JSON, etc.

6. Recursos y referencias recomendadas

Guía introductoria moderna a PHP — “The PHP Handbook” (online) — ideal para principiantes. 
freecodecamp.org

Manual oficial de PHP — sección de arrays: definición, uso, particularidades. 
php.net
+1

Tutoriales sobre JSON en PHP — uso de json_encode / json_decode. 
W3Schools
+2
W3Schools
+2

Artículos/tutoriales en español sobre arrays en PHP y su manipulación. 
manualweb.net
+1

7. Observaciones para la siguiente fase

Una vez superada esta introducción, los estudiantes estarán preparados para abordar temas más complejos: interaccionar con formularios, recibir datos, manipular ficheros o bases de datos, parsear entradas externas (por ejemplo correos), estructurar APIs REST, integrar con frontend JS.