# Introducción a JavaScript — Gestión de formularios

**Objetivo general:** aprender a crear scripts básicos en JavaScript que interactúen con formularios HTML.

---

## 1. Contexto y objetivos

JavaScript es el lenguaje que da interactividad a las páginas web.

| Capa | Función |
|------|----------|
| HTML | Estructura del contenido |
| CSS | Diseño y estilos |
| JavaScript | Lógica e interacción |

Qué haremos hoy:

- Crear variables y ejecutar código.
- Leer datos del usuario.
- Validar un formulario antes de enviarlo.

---

## 2. Primer contacto con el código

### Conceptos clave

- Etiqueta `<script>`: permite insertar JS en HTML.
- Lugares posibles:
  - Dentro del `<head>`.
  - Al final del `<body>` (recomendado).
- Salida de información:  
  `alert()`, `console.log()`, `document.write()`.

### Ejemplo 1 — Primer script

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mi primer script</title>
</head>
<body>
  <h1>Hola JavaScript</h1>

  <script>
    alert("¡Bienvenido a JavaScript!");
    console.log("Esto se muestra en la consola del navegador.");
    document.write("JavaScript está funcionando correctamente");
  </script>
</body>
</html>
```

### Actividad 1

1. Abre el archivo en tu navegador.  
2. Observa los tres tipos de salida.  
3. Explica la diferencia entre cada uno.

---

## 3. Variables y tipos de datos

### Conceptos variables y tipos

- Declaración:
  
  ```
  let nombre = "Ana";
  const PI = 3.14;
  var edad = 18;
  ```

- Tipos básicos:
    - `string` (texto)
    - `number` (número)
    - `boolean` (true / false)

- Concatenar texto:
    ```
    "Hola " + nombre
    ```

### Ejemplo 2 — Saludo personalizado

```html
<script>
  let nombre = prompt("¿Cómo te llamas?");
  let edad = prompt("¿Cuántos años tienes?");
  document.write("Hola " + nombre + ", tienes " + edad + " años.");
</script>
```

### Actividad 2

1. Ejecuta el script y observa el resultado.  
2. Añade una línea:

   ```js
   console.log(typeof edad);
   ```

3. ¿Qué tipo de dato devuelve? ¿Por qué?

---

## 4. Operaciones y lógica básica

### Conceptos

- Operadores aritméticos: `+`, `-`, `*`, `/`
- Operadores de comparación: `===`, `>`, `<`
- Condicionales:

  ```js
  if (condición) { ... } else { ... }
  ```

### Ejemplo 3 — Comparar números

```html
<script>
  let num1 = parseInt(prompt("Introduce un número:"));
  let num2 = parseInt(prompt("Introduce otro número:"));

  if (num1 > num2) {
    document.write(num1 + " es mayor que " + num2);
  } else if (num1 < num2) {
    document.write(num1 + " es menor que " + num2);
  } else {
    document.write("Ambos números son iguales");
  }
</script>
```

### Actividad 3

Modifica el código para mostrar si los números son pares o impares.  
Pista: usa `num1 % 2 === 0`

---

## 5. Interactuar con el DOM

### Conceptos DOM

La estructura de un documento HTML son las etiquetas (marcas).

Según el Modelo de Objetos del Documento (DOM), cada etiqueta HTML es un objeto. Las etiquetas anidadas son llamadas “hijas” de la etiqueta que las contiene. El texto dentro de una etiqueta también es un objeto.


```html

<!DOCTYPE HTML>
<html>
<body>
  The truth about elk.
  <ol>
    <li>An elk is a smart</li>
    <!-- comentario -->
    <li>...y el astuto animal!</li>
  </ol>
</body>
</html>
```

<div>
<div class="domtree"><svg width="690" height="500"><g transform="translate(20,30)"><path class="link" d="M7,0L7,30L32,30" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M7,0L7,60L32,60" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M32,60L32,90L57,90" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M32,60L32,120L57,120" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M32,60L32,420L57,420" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,150L82,150" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,180L82,180" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,240L82,240" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,270L82,270" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,300L82,300" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,330L82,330" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M57,120L57,390L82,390" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M82,180L82,210L107,210" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><path class="link" d="M82,330L82,360L107,360" style="fill: none; stroke: rgb(190, 195, 199); stroke-width: 1px;"></path><g class="node" transform="translate(0,0)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(206, 224, 244); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;">▾ </text><text dy="4.5" dx="16.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">HTML</text></g><g class="node" transform="translate(25,30)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(206, 224, 244); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;">▾ </text><text dy="4.5" dx="16.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">HEAD</text></g><g class="node" transform="translate(25,60)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(206, 224, 244); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;">▾ </text><text dy="4.5" dx="16.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">BODY</text></g><g class="node" transform="translate(50,90)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ↵␣␣The truth about elk.↵␣␣</text></g><g class="node" transform="translate(50,120)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(206, 224, 244); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;">▾ </text><text dy="4.5" dx="16.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">OL</text></g><g class="node" transform="translate(75,150)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ↵␣␣␣␣</text></g><g class="node" transform="translate(75,180)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(206, 224, 244); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;">▾ </text><text dy="4.5" dx="16.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">LI</text></g><g class="node" transform="translate(100,210)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text An elk is a smart</text></g><g class="node" transform="translate(75,240)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ↵␣␣␣␣</text></g><g class="node" transform="translate(75,270)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(207, 206, 149); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#comment comment</text></g><g class="node" transform="translate(75,300)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ↵␣␣␣␣</text></g><g class="node" transform="translate(75,330)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(206, 224, 244); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;">▾ </text><text dy="4.5" dx="16.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">LI</text></g><g class="node" transform="translate(100,360)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ...and cunning animal!</text></g><g class="node" transform="translate(75,390)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ↵␣␣</text></g><g class="node" transform="translate(50,420)" style="opacity: 1;"><rect y="-12.5" x="-5" rx="4" ry="4" height="25" width="280" style="fill: rgb(255, 222, 153); cursor: pointer;"></rect><text dy="4.5" dx="3.5" style="fill: black; pointer-events: none;"></text><text dy="4.5" dx="5.5" style="font: 14px Consolas, &quot;Lucida Console&quot;, Menlo, Monaco, monospace; fill: rgb(51, 51, 51); pointer-events: none;">#text ↵↵↵</text></g></g></svg></div>
</div>
[Fuente: Javscript.info](https://es.javascript.info/dom-nodes)

### Métodos y propiedades principales

#### Métodos

**getElementById**
  ```js
  document.getElementById("id")
  ```

- Podemos acceder a los elementos con getElementById
  - Devuelve el elemento con el atributo id especificado.
  - Es muy rápido y es el método más común cuando ya conoces el ID del elemento.


**querySelector**

  ```js
  document.querySelector(".descripcion");
  ```

- Podemos acceder a todos los elementos con la misma clase querySelector
  - Devuelve el primer elemento que coincide con el selector CSS dado.
  - Permite usar cualquier selector válido: #id, .clase, tag, combinados, etc.
  - Para obtener varios, existe querySelectorAll
  
#### Propiedades

**value**

```js
const nombre = document.getElementById("nombre").value;
```

Se usa principalmente en **inputs, textareas y selects**.  
Devuelve o establece **el valor introducido por el usuario**.

**innerText**

```js
titulo.innerText = "Nuevo título dinámico";
```

Representa **el texto visible dentro de un elemento HTML**.  
Tiene en cuenta estilos como `display: none` o `visibility: hidden`.

**style**

```js
parrafo.style.color = "blue";
parrafo.style.fontSize = "20px";
```

Permite modificar **estilos CSS en línea** del elemento mediante JavaScript.

### Ejemplo 4 — Leer un campo de texto

Tenemos que hablar  de los eventos para poder leer un campo de texto, pero...

## ¿Qué es un evento en JavaScript?

Un **evento** es cualquier acción o suceso que ocurre en la página web y que el navegador puede detectar.  
Tu código JavaScript puede **escuchar** esos eventos y **responder** ejecutando una función.

> **Un evento es una señal que indica que “algo ha pasado” en la página, como un clic, una tecla pulsada o la carga del documento.**

---

## Ejemplos de eventos comunes

- `click` — cuando el usuario hace clic en un elemento
- `input` — cuando el usuario escribe en un campo
- `submit` — cuando se envía un formulario
- `mouseover` — cuando el puntero entra en un elemento
- `keydown` — cuando se pulsa una tecla
- `load` — cuando la página ha terminado de cargarse

---

## ¿Cómo se usan los eventos?

Los eventos se gestionan mediante *manejadores de eventos* (**event listeners**):

```js
document.getElementById("boton").addEventListener("click", function() {
  console.log("¡Has hecho clic!");
});
```

En el ejemplo que vamos a trabajar:

```html
<body>
  <h2>Lectura del DOM</h2>
  <input type="text" id="nombre" placeholder="Escribe tu nombre">
  <button id="boton">Mostrar</button>
  <p id="resultado"></p>

  <script>
    const boton = document.getElementById("boton");
    const nombreInput = document.getElementById("nombre");
    const resultado = document.getElementById("resultado");

    boton.addEventListener("click", () => {
      const nombre = nombreInput.value;
      resultado.innerText = "Hola " + nombre;
    });
  </script>
</body>
```

### Actividad

Añade un campo edad y muestra un mensaje diferente según el valor:

- Si < 18 → “Eres menor de edad”
- Si ≥ 18 → “Eres mayor de edad”

---

## 6. Formularios y eventos

Un formulario (`<form>`) en HTML es un contenedor que agrupa campos donde el usuario puede introducir datos, como texto, correos, contraseñas, opciones o archivos.  
Es el elemento principal para recoger información y procesarla mediante JavaScript o enviarla a un servidor.

| Atributo       | Qué hace                                                      |
| -------------- | ------------------------------------------------------------- |
| `id`           | Identifica el formulario para manipularlo con JS              |
| `action`       | URL a la que se enviarán los datos (si se envían al servidor) |
| `method`       | Cómo se envían los datos (`GET` o `POST`)                     |
| `autocomplete` | Activar o desactivar sugerencias automáticas                  |
| `novalidate`   | Desactiva las validaciones automáticas del navegador          |

---

### Campos de un formulario

Los **campos de un formulario** son los elementos que permiten al usuario introducir información dentro de un `<form>`.  
Cada campo tiene un tipo que determina **qué datos recoge**, cómo se muestra y qué validaciones aplica automáticamente el navegador.

> **Los campos de un formulario son elementos interactivos que permiten escribir, seleccionar o enviar datos en una página web.**

Los más comunes se crean con elementos como:

- `<input type="...">`
- `<textarea>`
- `<select>`
- `<button>`

#### 1. `input type="text"`
```html
<input type="text" placeholder="Nombre">
```

#### 2. `textarea`
```html
<textarea placeholder="Escribe tu mensaje"></textarea>
```

#### 3. `input type="number"`
```html
<input type="number" min="1" max="100">
```

#### 4. `input type="password"`
```html
<input type="password" placeholder="Contraseña">
```

#### 5. `input type="email"`
```html
<input type="email" placeholder="correo@ejemplo.com">
```

#### 6. `input type="date"`
```html
<input type="date">
```

#### 7. `input type="checkbox"`
```html
<input type="checkbox"> Acepto los términos
```

#### 8. `input type="radio"`
```html
<input type="radio" name="color" value="rojo"> Rojo
```

#### 9. `select` y `option`
```html
<select>
  <option>España</option>
  <option>Francia</option>
  <option>Italia</option>
</select>
```

---

### Eventos asociados a un formulario

Cuando un usuario interactúa con una página web —escribe en un formulario, hace clic en un botón o selecciona una opción— ocurren eventos. Gracias a los eventos, podemos validar formularios, mostrar mensajes, actualizar información o evitar errores.

| Evento | Dónde se usa | Cuándo ocurre | Ejemplo práctico |
|--------|--------------|----------------|------------------|
| `submit` | `<form>` | Al enviar el formulario | Validar antes de enviar |
| `reset` | `<form>` | Al reiniciar | Limpiar mensajes |
| `input` | `input`, `textarea` | Mientras escribe | Contador de caracteres |
| `change` | `input`, `select`, `checkbox`, `radio` | Cambio + perder foco | Cambiar opción |
| `focus` | campos | Al recibir foco | Resaltar campo |
| `blur` | campos | Al perder foco | Validar campo |
| `keydown` / `keyup` | texto | Pulsar teclas | Validación en tiempo real |
| `click` | botones, checkbox, radio | Clic | Activar opciones |
| `invalid` | campos HTML5 | Falla validación | Mensaje automático |

---

## De los conceptos a la práctica

### Pasos para controlar un formulario

1. Seleccionar el formulario.  
2. Escuchar el evento `submit`.  
3. Usar `event.preventDefault()`.  
4. Leer valores con `.value`.  
5. Validar los datos.  
6. Mostrar mensajes.  
7. Resetear si es necesario.

Ejemplo mínimo:

```js
form.addEventListener("submit", (event) => {
  event.preventDefault();
  console.log("Intento de envío detectado");
});
```

---

### Ejemplo Completo — Formulario con validación

```html
<body>
  <h2>Formulario de contacto</h2>
  <form id="formulario">
    <input type="text" id="nombre" placeholder="Nombre"><br>
    <input type="email" id="email" placeholder="Correo"><br>
    <button type="submit">Enviar</button>
  </form>

  <p id="mensaje"></p>

  <script>
    const form = document.getElementById("formulario");
    const mensaje = document.getElementById("mensaje");

    form.addEventListener("submit", (event) => {
      event.preventDefault();

      const nombre = document.getElementById("nombre").value.trim();
      const email = document.getElementById("email").value.trim();

      if (nombre === "" || email === "") {
        mensaje.innerText = "Rellena todos los campos.";
        mensaje.style.color = "red";
      } else {
        mensaje.innerText = "Formulario enviado correctamente.";
        mensaje.style.color = "green";
        form.reset();
      }
    });
  </script>
</body>
```
