# Practica

1. El cliente (HTML + JS) muestra un formulario.  
2. El usuario rellena los campos y envía los datos.  
3. JavaScript captura el envío y manda los datos al servidor (PHP) mediante `fetch()` usando `POST`.  
4. PHP recibe los datos desde `$_POST`, los procesa y devuelve una respuesta en JSON.  
5. JavaScript recibe el JSON y muestra un mensaje o un resumen en la página.

Representación simplificada:

```
Usuario → Formulario HTML/JS → PHP (procesa) → JSON → JavaScript → Vista HTML
```

---

# 2. Crear un formulario HTML

Archivo: **index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Registro de curso</title>
</head>
<body>

<h1>Formulario de registro</h1>

<form id="form-registro">
    <label>
        Nombre:
        <input type="text" name="nombre" required>
    </label>
    <br>

    <label>
        Email:
        <input type="email" name="email" required>
    </label>
    <br>

    <label>
        Edad:
        <input type="number" name="edad" required>
    </label>
    <br>

    <label>
        Curso:
        <input type="text" name="curso" required>
    </label>
    <br>

    <button type="submit">Enviar</button>
</form>

<div id="resultado"></div>

<script src="script.js"></script>
</body>
</html>
```

---

# 3. Enviar los datos con fetch() (POST)

Archivo: **script.js**

```js
const form = document.getElementById("form-registro");
const divResultado = document.getElementById("resultado");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);

    fetch("procesar.php", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        let html = "";

        if (data.ok) {
            html += "<h2>Registro correcto</h2>";
            html += "<p>Nombre: " + data.datos.nombre + "</p>";
            html += "<p>Email: " + data.datos.email + "</p>";
            html += "<p>Edad: " + data.datos.edad + "</p>";
            html += "<p>Curso: " + data.datos.curso + "</p>";
            html += "<p>Mensaje: " + data.mensaje + "</p>";
        } else {
            html += "<h2>Se produjo un error</h2>";
            html += "<p>" + data.mensaje + "</p>";
        }

        divResultado.innerHTML = html;
    });
});
```

---

# 4. Recibir y procesar los datos en PHP

Archivo: **procesar.php**

```php
<?php
// Opcional: forzar cabecera JSON
header("Content-Type: application/json; charset=utf-8");

// Recibir datos desde POST
$nombre = $_POST["nombre"] ?? "";
$email  = $_POST["email"] ?? "";
$edad   = $_POST["edad"] ?? "";
$curso  = $_POST["curso"] ?? "";

// Validación mínima
if ($nombre === "" || $email === "" || $edad === "" || $curso === "") {
    $respuesta = [
        "ok" => false,
        "mensaje" => "Faltan datos en el formulario."
    ];
} else {
    // Crear array asociativo con los datos
    $datos = [
        "nombre" => $nombre,
        "email"  => $email,
        "edad"   => (int)$edad,
        "curso"  => $curso
    ];

    $respuesta = [
        "ok" => true,
        "mensaje" => "Datos recibidos correctamente.",
        "datos" => $datos
    ];
}

// Devolver respuesta en JSON
echo json_encode($respuesta);
```

---

# 5. Actividades guiadas

## Actividad 1 — Añadir campo extra
Añadir al formulario un campo `comentarios` y hacer que:

- Se envíe a PHP.
- Se añada al array `$datos`.
- Se muestre en la respuesta JSON y en la página.

---

## Actividad 2 — Validación de edad

Modificar `procesar.php` para que:

- Si la edad es menor de 18, `ok` sea `false` y el mensaje sea:  
  `"Debes ser mayor de edad para registrarte."`
- Si es 18 o más, se procese normalmente.

---

## Actividad 3 — Mostrar errores en rojo

En `script.js`, si `data.ok` es `false`, mostrar el mensaje de error en rojo (añadiendo una clase o estilo inline).

---

# 6. Mini-proyecto de fin de sesión (versión basada en formulario)

Crear una mini-aplicación llamada **registro-curso/** con los siguientes archivos:

## 6.1 Archivos requeridos

### **index.html**
- Contiene un formulario con los campos:
  - nombre  
  - email  
  - edad  
  - curso  
- Incluye el archivo `script.js`.
- Dispone de un `<div id="resultado"></div>` para mostrar la respuesta.

### **script.js**

- Captura el envío del formulario.
- Envía los datos mediante `fetch()` con método `POST` a `procesar.php`.
- Recibe la respuesta JSON.
- Muestra en el `<div id="resultado">` un resumen de los datos recibidos y el mensaje devuelto.

### **procesar.php**

- Recibe los datos usando `$_POST`.
- Realiza validaciones mínimas (no vacío, edad numérica, etc.).
- Crea un array asociativo con los datos.
- Construye una respuesta del tipo:

```php
$respuesta = [
    "ok" => true,
    "mensaje" => "Registro guardado correctamente.",
    "datos" => [
        "nombre" => "...",
        "email" => "...",
        "edad" => 0,
        "curso" => "..."
    ]
];
```

- Devuelve la respuesta con `echo json_encode($respuesta);`.

## 6.2 Resultados esperados

- El formulario se envía **sin recargar la página** (gracias a JavaScript y `fetch()`).
- Si faltan datos o hay errores, se muestra un mensaje adecuado.
- Si todo es correcto, se muestra un resumen claro de la información enviada.

Se deberá utilizar:
- Variables y arrays asociativos en PHP.  
- `json_encode()` para responder al cliente.  
- `fetch()` y manejo de JSON en JavaScript.  
- Manipulación del DOM para mostrar resultados.
