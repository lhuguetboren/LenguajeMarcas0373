# Práctica inicial — Introducción a JavaScript

## Objetivo

Comprender y practicar los fundamentos del lenguaje JavaScript:

- Cómo incluir código JS en una página HTML.
- Cómo declarar variables y mostrar información.
- Cómo realizar operaciones simples.
- Cómo usar condiciones y funciones básicas.
- Cómo mostrar resultados en pantalla o en la consola.

---

## 1. Estructura base de un documento con JavaScript

Crea un archivo llamado **`index.html`** con el siguiente contenido:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Práctica JavaScript</title>
</head>
<body>
  <h1>Mi primera práctica con JavaScript</h1>

  <script>
    // Aquí escribiremos nuestro código
    alert("Bienvenido al mundo de JavaScript");
    console.log("Este mensaje aparece en la consola");
    document.write("<p>JavaScript está funcionando correctamente</p>");
  </script>
</body>
</html>
```

**Tareas:**

1. Abre el archivo en el navegador.  
2. Explica qué hace cada línea (`alert`, `console.log`, `document.write`).  
3. Añade un comentario en el código explicando qué aprendiste.

**Amplía:**  
[W3Schools - Introducción a JavaScript](https://www.w3schools.com/js/js_intro.asp)

---

## 2. Variables y tipos de datos

En el mismo archivo, sustituye el contenido del `<script>` por lo siguiente:

```html
<script>
  let nombre = "Ana";
  let edad = 20;
  const PI = 3.1416;

  document.write("<p>Hola, " + nombre + ". Tienes " + edad + " años.</p>");
  document.write("<p>El valor de PI es: " + PI + "</p>");
</script>
```

**Tareas:**

1. Cambia los valores de las variables y observa los resultados.  
2. Añade una nueva variable llamada `ciudad` y muéstrala en pantalla.  
3. Experimenta con `console.log()` para mostrar las variables en la consola.

**Amplía:**  
[W3Schools - Variables](https://www.w3schools.com/js/js_variables.asp)  
[W3Schools - Tipos de datos](https://www.w3schools.com/js/js_datatypes.asp)

---

## 3. Operaciones y condicionales

Modifica el script para incluir operaciones simples:

```html
<script>
  let num1 = 10;
  let num2 = 5;

  let suma = num1 + num2;
  let resta = num1 - num2;

  document.write("<p>La suma es: " + suma + "</p>");
  document.write("<p>La resta es: " + resta + "</p>");

  if (num1 > num2) {
    document.write("<p>" + num1 + " es mayor que " + num2 + "</p>");
  } else {
    document.write("<p>" + num1 + " no es mayor que " + num2 + "</p>");
  }
</script>
```

**Tareas:**

1. Cambia los valores y prueba otras operaciones (`*`, `/`, `%`).  
2. Crea una condición que indique si un número es par o impar.

**Amplía:**  
[W3Schools - Operadores](https://www.w3schools.com/js/js_operators.asp)  
[W3Schools - Condicionales](https://www.w3schools.com/js/js_if_else.asp)

---

## 4. Funciones básicas

Agrega una pequeña función para saludar al usuario:

```html
<script>
  function saludar(nombre) {
    return "Hola, " + nombre + "!";
  }

  let mensaje = saludar("Carlos");
  document.write("<p>" + mensaje + "</p>");
</script>
```

**Tareas:**

1. Cambia el nombre pasado a la función.  
2. Crea una función que calcule el cuadrado de un número (`n * n`) y la muestre.

**Amplía:**  
[W3Schools - Funciones](https://www.w3schools.com/js/js_functions.asp)

---

## 5. Entrada de datos con `prompt()`

Permite que el usuario introduzca información:

```html
<script>
  let nombre = prompt("¿Cómo te llamas?");
  document.write("<h2>Bienvenido, " + nombre + "!</h2>");
</script>
```

**Tareas:**

1. Añade otro `prompt` para pedir la edad.  
2. Muestra un mensaje distinto si el usuario tiene menos de 18 años.

**Amplía:**  
[W3Schools - Ventanas emergentes](https://www.w3schools.com/js/js_popup.asp)

---

## 6. Conclusión

Con esta práctica ya has utilizado:

- Variables (`let`, `const`).
- Operaciones y condiciones.
- Funciones.
- Salida en pantalla (`document.write`, `console.log`, `alert`).
- Entrada de datos (`prompt`).

A partir de aquí puedes continuar con ejercicios interactivos en:  
[W3Schools JavaScript Exercises](https://www.w3schools.com/js/exercise_js.asp)
