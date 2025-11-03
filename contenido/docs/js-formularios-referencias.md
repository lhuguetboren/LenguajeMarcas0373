# Glosario y referencias— Elementos de JavaScript y HTML utilizados

## 1. Elementos HTML

| Elemento | Descripción | Ejemplo / Uso |
|-----------|-------------|---------------|
| `<!DOCTYPE html>` | Indica al navegador que el documento está escrito en HTML5. | `<!DOCTYPE html>` |
| `<html>` | Elemento raíz del documento HTML. Contiene todo el contenido de la página. | `<html lang="es"> ... </html>` |
| `<head>` | Contiene metadatos, enlaces a CSS o JS, y el título de la página. | `<head><title>Mi página</title></head>` |
| `<meta charset="UTF-8">` | Define la codificación de caracteres (UTF-8 permite tildes y ñ). | `<meta charset="UTF-8">` |
| `<title>` | Define el título que aparece en la pestaña del navegador. | `<title>Ejemplo JS</title>` |
| `<body>` | Contiene todo el contenido visible del documento. | `<body>...</body>` |
| `<h1>`, `<h2>` | Encabezados de diferentes niveles. `<h1>` es el principal, `<h2>` un subtítulo. | `<h1>Hola</h1>` |
| `<p>` | Párrafo de texto. | `<p>Texto de ejemplo</p>` |
| `<input>` | Campo de entrada de datos en formularios. Puede ser de distintos tipos. | `<input type="text" id="nombre">` |
| `type` (atributo) | Define el tipo de entrada (`text`, `email`, `number`, etc.). | `<input type="email">` |
| `id` (atributo) | Identificador único del elemento, usado por JavaScript. | `<input id="nombre">` |
| `placeholder` | Texto que aparece como ejemplo dentro del campo hasta que el usuario escribe. | `<input placeholder="Escribe tu nombre">` |
| `<button>` | Crea un botón que puede ejecutar código o enviar formularios. | `<button id="boton">Enviar</button>` |
| `<form>` | Agrupa campos y botones de un formulario. | `<form id="formulario"> ... </form>` |
| `<br>` | Salto de línea. | `<input><br><input>` |
| `<script>` | Define o enlaza código JavaScript dentro del documento HTML. | `<script> ... </script>` |

---

## 2. Elementos y métodos de JavaScript

### 2.1. Funciones básicas de salida y entrada
| Función / Método | Descripción | Ejemplo |
|------------------|-------------|----------|
| `alert()` | Muestra un cuadro de diálogo emergente con un mensaje. | `alert("Hola mundo");` |
| `console.log()` | Muestra mensajes en la consola del navegador (útil para depurar). | `console.log("Prueba");` |
| `document.write()` | Escribe directamente contenido en la página. | `document.write("Texto en pantalla");` |
| `prompt()` | Solicita al usuario que introduzca un valor mediante una ventana emergente. | `let nombre = prompt("¿Tu nombre?");` |

---

### 2.2. Variables y tipos de datos
| Palabra clave | Descripción | Ejemplo |
|----------------|-------------|----------|
| `let` | Declara una variable con ámbito de bloque. | `let edad = 20;` |
| `const` | Declara una constante (no se puede reasignar). | `const PI = 3.14;` |
| `var` | Forma antigua de declarar variables (ámbito de función). | `var nombre = "Ana";` |
| `typeof` | Devuelve el tipo de dato de una variable. | `typeof 3` → `"number"` |

**Tipos de datos vistos:**
- `string` → cadenas de texto (`"Hola"`)
- `number` → números (`42`)
- `boolean` → verdadero o falso (`true`, `false`)

---

### 2.3. Operadores
| Tipo | Operadores | Ejemplo | Descripción |
|------|-------------|----------|-------------|
| Aritméticos | `+`, `-`, `*`, `/`, `%` | `5 + 2` → `7` | Operaciones matemáticas. `%` devuelve el resto. |
| Comparación | `===`, `>`, `<`, `>=`, `<=` | `a > b` | Devuelven `true` o `false`. |
| Lógicos | `&&`, `||`, `!` | `a > 0 && b < 5` | Combinan condiciones booleanas. |

---

### 2.4. Condicionales
| Estructura | Descripción | Ejemplo |
|-------------|-------------|----------|
| `if` / `else if` / `else` | Evalúa condiciones y ejecuta bloques según el resultado. | ```js if (x > 0) { ... } else { ... } ``` |

---

### 2.5. Funciones y eventos
| Elemento | Descripción | Ejemplo |
|-----------|-------------|----------|
| `function` | Define una función reutilizable. | ```js function saludar() { alert("Hola"); } ``` |
| `addEventListener()` | Asocia un evento (click, submit, etc.) a una función. | `boton.addEventListener("click", mostrar);` |
| `event.preventDefault()` | Evita la acción por defecto de un evento (por ejemplo, que un formulario se envíe). | `event.preventDefault();` |

**Eventos usados:**
- `"click"` → al hacer clic en un botón.  
- `"submit"` → al enviar un formulario.

---

### 2.6. Acceso y manipulación del DOM
| Método / Propiedad | Descripción | Ejemplo |
|---------------------|-------------|----------|
| `document.getElementById("id")` | Selecciona un elemento por su atributo `id`. | `const campo = document.getElementById("nombre");` |
| `document.querySelector("selector")` | Selecciona el primer elemento que cumpla el selector CSS indicado. | `document.querySelector("p");` |
| `.value` | Devuelve o cambia el valor de un campo de formulario. | `nombre.value = "Joan";` |
| `.innerText` | Devuelve o modifica el texto visible dentro de un elemento. | `p.innerText = "Hola";` |
| `.style` | Permite modificar propiedades CSS desde JavaScript. | `p.style.color = "red";` |
| `.trim()` | Elimina espacios en blanco al principio y final de una cadena. | `" hola ".trim()` → `"hola"` |
| `.reset()` | Limpia todos los campos de un formulario. | `form.reset();` |

---

### 2.7. Conversión y manipulación de datos
| Método / Función | Descripción | Ejemplo |
|------------------|-------------|----------|
| `parseInt()` | Convierte una cadena en número entero. | `parseInt("42")` → `42` |
| `+variable` | Convierte un string numérico en número. | `+"10"` → `10` |
| Concatenación (`+`) | Une textos o valores. | `"Hola " + nombre` |

---

## 3. Buenas prácticas vistas en los ejemplos

| Concepto | Explicación |
|-----------|-------------|
| Separar el JavaScript del HTML | Mantener el código JS en archivos `.js` externos cuando crezcan los proyectos. |
| Nombrar los elementos con `id` claros | Facilita el acceso a los elementos desde el script. |
| Usar `const` y `let` en lugar de `var` | Mejora la legibilidad y reduce errores. |
| Validar datos antes de enviar un formulario | Previene errores y mejora la experiencia del usuario. |
| Usar `console.log()` para depurar | Permite comprobar valores sin interrumpir la ejecución. |

---

## 4. Resumen general de conceptos introducidos

- HTML: estructura del documento y elementos visibles.  
- DOM: representación interna que JavaScript usa para acceder y modificar la página.  
- Eventos: acciones del usuario (click, submit, etc.) que el script puede detectar.  
- Variables: almacenamiento de datos temporales.  
- Condicionales: ejecución de código según condiciones.  
- Funciones: agrupación de instrucciones reutilizables.  
- Validación de formularios: comprobación de datos antes del envío.

## 5. Referencias aprendizaje JavaScript

| Tipo | Nombre / Enlace | Idioma | Descripción |
|------|------------------|---------|--------------|
| Web | [Tutorial JavaScript](https://www.w3schools.com/js/) | Inglés | Teoría y práctica |
| Web | [Aprende JavaScript](https://www.aprendejavascript.dev) | Español | Curso gratuito paso a paso desde cero, con ejemplos interactivos. |
| Web | [Curso de JavaScript - Soy Henry](https://www.soyhenry.com/curso-javascript?utm_source=chatgpt.com) | Español | Curso gratuito introductorio con fundamentos del lenguaje y ejercicios. |
| Web | [El Tutorial de JavaScript Moderno](https://es.javascript.info) | Español | Tutorial muy completo y actualizado, desde lo básico hasta avanzado. |
| Web | [Curs de JavaScript - Albert Vila](https://albertvila.cat/curs-javascript/02.htm?utm_source=chatgpt.com) | Catalán | Tutorial en catalán con explicaciones claras y ejemplos básicos. |
| Video | [Curso de JavaScript desde Cero - freeCodeCamp Español](https://www.freecodecamp.org/espanol/news/aprende-javascript-curso-completo-desde-cero) | Español | Curso completo gratuito en vídeo, ideal para principiantes. |
| Video | [Curso completo de JavaScript desde cero - YouTube](https://www.youtube.com/watch?v=1glVfFxj8a4&utm_source=chatgpt.com) | Español | Curso en YouTube con teoría y práctica paso a paso. |
