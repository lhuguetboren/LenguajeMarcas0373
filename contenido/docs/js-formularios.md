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

- El DOM (Document Object Model) es la estructura interna del HTML.  
- Podemos acceder a los elementos:

  ```js
  document.getElementById("id")
  document.querySelector("selector")
  ```

- Propiedades comunes:
  - `.value`
  - `.innerText`
  - `.style`

### Ejemplo 4 — Leer un campo de texto

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

### Conceptos Formularios

- El evento `submit` se lanza al enviar un formulario.
- `event.preventDefault()` impide el envío real.
- Validar datos = comprobar que no estén vacíos o que cumplan un formato.

### Ejemplo 5 — Formulario con validación

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

### Actividad 4

1. Prueba el formulario sin rellenar → mensaje de error.  
2. Rellénalo → mensaje de éxito.  
3. Añade una validación que compruebe que el correo contiene “@”.

---

## Actividad final

Crea un formulario con los campos:

- Nombre  
- Edad  
- Email  
- Comentario  

Valida que:

- Todos los campos estén completos.
- La edad sea un número mayor que 0.  
- El email contenga `@`.  

Si todo es correcto, muestra un mensaje personalizado en pantalla.
