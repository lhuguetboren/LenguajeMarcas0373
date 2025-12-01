# Introducción a PHP



``` mermaid
flowchart LR
  A[Introducción a PHP] --> B[Teoría]
  A --> C[Aplicación]

  %% TEORÍA
  B --> B1[PHP como lenguaje de servidor]
  B --> B2[Procesamiento cliente-servidor]
  B --> B3[Etiquetas PHP dentro de HTML]
  B --> B4[Salida dinámica con echo/print]

  %% APLICACIÓN
  C --> C1[Crear archivo .php y ejecutarlo]
  C --> C2[Insertar PHP en HTML]
  C --> C3[Probar en servidor local]
  C --> C4[Imprimir texto y valores]
```

# 1. Qué es PHP

PHP es un lenguaje de programación del lado del servidor usado para desarrollar aplicaciones web dinámicas. Mientras HTML y JS se ejecutan en el navegador (cliente), PHP se ejecuta en el servidor y genera contenido que luego se envía al navegador.

Características:

- Lenguaje interpretado en servidor.
- El código se ejecuta antes de llegar al navegador.
- Puede generar HTML, JSON o texto.
- Trabaja con archivos, bases de datos y APIs.

## Instalación XAMPP

[Instrucciones](https://www.apachefriends.org/es/faq_windows.html)
[Web Instalar paso a paso](https://www.youtube.com/watch?v=sFI7ck-j9iw)

# 2. Cliente vs Servidor

Cliente (navegador):
- HTML, CSS, JS  
- Renderiza la interfaz  
- Ejecuta JavaScript  

Servidor (PHP):
- Ejecuta scripts PHP
- Procesa datos
- Conecta con bases de datos
- Genera HTML o JSON

Flujo básico:
1. El navegador pide una URL (`http://localhost/index.php`).
2. El servidor ejecuta el archivo `.php`.
3. Envía al navegador solo el resultado (HTML/JSON).
4. El navegador no recibe el código PHP.

# 3. La etiqueta de PHP
Todo código PHP se escribe entre:

```php
<?php

?>
```

# 4. Primer ejemplo de PHP

```php
<?php
echo "Hola desde PHP!";

?>```
# 5. PHP incrustado en HTML

```php
<!DOCTYPE html>
<html>
<head>
    <title>Mi primera página PHP</title>
</head>
<body>

<h1>Página generada con PHP</h1>

<p>
    <?php
        echo "Este texto fue generado por PHP.";
    ?>
</p>

<p>
    Hoy es: 
    <?php
        echo date("d/m/Y");
    ?>
</p>

</body>
</html>
```

# 6. Comentarios en PHP

```php
<?php
// Comentario de una línea
# Otro comentario
/*
 Comentario de varias líneas
*/
```

# 7. Cómo ejecutar código PHP

1. Instalar XAMPP / WAMP / MAMP o PHP CLI.  
2. Guardar archivos `.php` en la carpeta del servidor.  
3. Abrir en el navegador: `http://localhost/lm/index.php`.

# 8. Actividades guiadas

## Actividad 1 — Página dinámica básica
Crear una página que combine HTML y PHP usando `echo`.

## Actividad 2 — Mostrar fecha y hora del servidor
```php
<?php
echo "Fecha actual: " . date("d/m/Y H:i:s");
?>
```

## Actividad 3 — Ver código fuente
Comprobar que el navegador no muestra código PHP.

# 9. Reto final
Crear un archivo `perfil.php` que:

- Muestre un encabezado HTML
- Salude usando PHP
- Muestre la fecha actual
- Indique la ruta del archivo usando `__FILE__`
