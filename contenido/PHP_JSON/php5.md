# Flujo cliente–servidor

1. El cliente (HTML + JS) solicita datos a un archivo PHP.  
2. PHP genera o carga los datos y los devuelve en formato JSON.  
3. JavaScript recibe el JSON, lo procesa y lo muestra en la página.

Representación simplificada:

```
HTML/JS (cliente) → petición → PHP (servidor)
HTML/JS (cliente) ← JSON ← PHP (servidor)
```

---

# 2. Crear un endpoint PHP que devuelva JSON

Archivo: **productos.php**

```php
<?php
$productos = [
    "Laptop" => 799,
    "Teclado" => 25,
    "Ratón"   => 15
];

header("Content-Type: application/json");
echo json_encode($productos);
?>
```

Este archivo actúa como “API” mínima.

---

# 3. Consumir JSON desde JavaScript con fetch()

Archivo: **index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Catálogo</title>
</head>
<body>

<h1>Catálogo desde PHP</h1>
<div id="lista"></div>

<script>
fetch("productos.php")
    .then(res => res.json())
    .then(data => {
        let html = "<ul>";

        for (const producto in data) {
            html += "<li>" + producto + " — " + data[producto] + " €</li>";
        }

        html += "</ul>";
        document.getElementById("lista").innerHTML = html;
    });
</script>

</body>
</html>
```

---

# 4. Mostrar datos dinámicos en HTML

El navegador recibiría algo como:

```json
{"Laptop":799,"Teclado":25,"Ratón":15}
```

Que JavaScript transforma automáticamente en una lista.

---

# 5. Actividades guiadas

## Actividad 1 — Crear tu primer endpoint
En un archivo **info.php**, devolver:

- nombre  
- curso  
- año  
- horario  

Ejemplo JSON esperado:

```
{"nombre":"PHP Básico","año":2025}
```

Consumirlo con `fetch()` desde HTML.

---

## Actividad 2 — Mostrar resultados en una tabla

1. Crear un array asociativo en PHP con:
   - país  
   - capital  
   - población  

2. Devolverlo como JSON.  
3. Mostrarlo con JavaScript en una tabla HTML.

---

## Actividad 3 — Añadir estilos

Diseñar la página HTML con estilos simples (CSS integrado o archivo externo).

---

# 6. Mini-reto de fin de sesión

Crear una mini-aplicación llamada **tienda-online/** con:

## 6.1 Archivos requeridos

### **productos.php**
Devuelve un array asociativo con tres productos y sus precios.

### **index.html**

- Contiene un botón: **“Cargar productos”**
- Al hacer clic, JavaScript ejecuta un `fetch()` a `productos.php`
- Muestra los productos en una tabla

### **script.js**

- Realiza la petición usando `fetch`
- Rellena la tabla dinámicamente

## 6.2 Resultados esperados

Tabla similar a:

```
Producto     | Precio
----------------------
Laptop       | 799 €
Teclado      | 25 €
Ratón        | 15 €
```

El alumno deberá utilizar:

- Arrays simples  
- json_encode  
- fetch  
- Manipulación del DOM  

---
