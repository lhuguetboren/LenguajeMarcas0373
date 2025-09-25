
# Atributos para tags de HTML

Los atributos añaden información extra a las etiquetas y se colocan en el **tag de apertura**.

### Ejemplos:

- **`href` en `<a>` (enlaces):**
```html
<a href="https://www.wikipedia.org" target="_blank">Ir a Wikipedia</a>
```

- **`src` en `<img>` (imágenes):**
```html
<img src="paisaje.jpg" alt="Foto de un paisaje" width="300" />
```

- **`rel` en `<link>` (archivos externos como CSS):**
```html
<link rel="stylesheet" href="estilos.css">
```

## Atributos clave: id, class y style

- **`id`**: identificador único.  
- **`class`**: agrupa varios elementos.  
- **`style`**: aplicar estilos en línea.

Ejemplo:

```html
<p id="parrafo1" class="destacado" style="color: blue; font-size: 18px;">
  Este es un párrafo con id, class y estilo en línea.
</p>
```

| Propiedad          | Descripción                                        | Ejemplo                                                                   |
| ------------------ | -------------------------------------------------- | ------------------------------------------------------------------------- |
| `color`            | Define el color del texto.                         | `<p style="color: red;">Texto rojo</p>`                                   |
| `background-color` | Color de fondo del elemento.                       | `<p style="background-color: yellow;">Fondo amarillo</p>`                 |
| `font-size`        | Tamaño de la fuente.                               | `<p style="font-size: 20px;">Texto grande</p>`                            |
| `font-family`      | Tipo de letra.                                     | `<p style="font-family: Arial;">Texto en Arial</p>`                       |
| `font-weight`      | Grosor de la fuente (normal, bold).                | `<p style="font-weight: bold;">Negrita</p>`                               |
| `font-style`       | Estilo de la fuente (normal, italic).              | `<p style="font-style: italic;">Cursiva</p>`                              |
| `text-align`       | Alineación del texto (left, center, right).        | `<p style="text-align: center;">Centrado</p>`                             |
| `text-decoration`  | Decoración (underline, line-through, none).        | `<p style="text-decoration: underline;">Subrayado</p>`                    |
| `line-height`      | Espacio vertical entre líneas.                     | `<p style="line-height: 2;">Espaciado doble</p>`                          |
| `letter-spacing`   | Espacio entre letras.                              | `<p style="letter-spacing: 3px;">T e x t o</p>`                           |
| `word-spacing`     | Espacio entre palabras.                            | `<p style="word-spacing: 10px;">Más espacio entre palabras</p>`           |
| `margin`           | Margen exterior del elemento.                      | `<p style="margin: 20px;">Con margen</p>`                                 |
| `padding`          | Espacio interior del elemento.                     | `<p style="padding: 15px; background: lightgray;">Con padding</p>`        |
| `border`           | Borde alrededor del elemento.                      | `<p style="border: 2px solid black;">Con borde</p>`                       |
| `border-radius`    | Esquinas redondeadas.                              | `<p style="border: 2px solid black; border-radius: 10px;">Redondeado</p>` |
| `width`            | Ancho del elemento.                                | `<div style="width: 200px; background: lightblue;">200px</div>`           |
| `height`           | Alto del elemento.                                 | `<div style="height: 100px; background: lightgreen;">100px</div>`         |
| `display`          | Tipo de visualización (block, inline, flex, none). | `<span style="display: block; background: yellow;">Bloque</span>`         |
| `position`         | Posicionamiento (relative, absolute, fixed…).      | `<div style="position: relative; top: 20px;">Caja movida</div>`           |
| `opacity`          | Transparencia (0 a 1).                             | `<p style="opacity: 0.5;">Semi-transparente</p>`                          |

---

## Etiquetas y atributos HTML más comunes

A continuación se presentan las 20 etiquetas más comunes de HTML, cada una con una breve explicación y un ejemplo práctico.

---

## 1. `<!DOCTYPE html>`

Declara el tipo de documento y la versión de HTML (HTML5 en este caso). Siempre debe ir al inicio del archivo.

```html
<!DOCTYPE html>
```

---

## 2. `<html>`

Etiqueta raíz que envuelve todo el contenido de la página.

```html
<html lang="es"> ... </html>
```

---

## 3. `<head>`

Contiene información de configuración y metadatos (no se muestra en la página).

```html
<head>
  <meta charset="UTF-8">
  <title>Ejemplo head</title>
</head>
```

---

## 4. `<title>`

Define el título que aparece en la pestaña del navegador.

```html
<title>Mi página</title>
```

---

## 5. `<meta>`

Proporciona metadatos como la codificación de caracteres o la descripción.

```html
<meta charset="UTF-8">
```

---

## 6. `<body>`

Contiene todo el contenido visible de la página.

```html
<body>Contenido visible</body>
```

---

## 7. `<h1> ... <h6>`

Encabezados jerárquicos, desde el más importante (`h1`) hasta el menos (`h6`).

```html
<h1>Título principal</h1>
<h2>Subtítulo</h2>
```

---

## 8. `<p>`

Define un párrafo de texto.

```html
<p>Este es un párrafo</p>
```

---

## 9. `<a>`

Crea un enlace a otra página o recurso.

```html
<a href="https://www.google.com" target="_blank">Ir a Google</a>
```

---

## 10. `<img>`

Inserta una imagen en la página.

```html
<img src="foto.jpg" alt="Descripción" width="200">
```

---

## 11. `<ul>` y `<li>`

Crea una lista desordenada (con viñetas).

```html
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ul>
```

---

## 12. `<ol>` y `<li>`

Crea una lista ordenada (numerada).

```html
<ol>
  <li>Paso 1</li>
  <li>Paso 2</li>
</ol>
```

---

## 13. `<div>`

Contenedor genérico en bloque, útil para maquetar.

```html
<div style="background: lightblue; padding: 10px;">
  <p>Contenido dentro de un div</p>
</div>
```

---

## 14. `<span>`

Contenedor en línea para aplicar estilos a parte del texto.

```html
<p>Texto con <span style="color:red;">span destacado</span></p>
```

---

## 15. `<br>`

Inserta un salto de línea.

```html
Línea 1<br>Línea 2
```

---

## 16. `<hr>`

Inserta una línea horizontal divisoria.

```html
<p>Texto arriba</p>
<hr>
<p>Texto abajo</p>
```

---

## 17. `<strong>`

Indica texto con importancia (normalmente en negrita).

```html
<p>Texto <strong>importante</strong></p>
```

---

## 18. `<em>`

Resalta texto con énfasis (normalmente en cursiva).

```html
<p>Texto con <em>énfasis</em></p>
```

---

## 19. `<table>`, `<tr>`, `<td>`, `<th>`

Permite crear tablas con filas, columnas y cabeceras.

```html
<table border="1">
  <tr>
    <th>Nombre</th><th>Edad</th>
  </tr>
  <tr>
    <td>Ana</td><td>22</td>
  </tr>
</table>
```

## Uso del `<div>` para maquetación

El `<div>` es una etiqueta de HTML que sirve como contenedor genérico en bloque.
No añade ningún estilo ni significado por sí mismo, pero se utiliza para agrupar otros elementos y organizarlos en la página, normalmente aplicando estilos con CSS o funciones con JavaScript.

Piensa en él como una caja vacía donde puedes meter texto, imágenes u otras etiquetas para darles formato o estructura.

### Ejemplo básico

```html
<div>
  <p>Esto es un bloque dentro de un div.</p>
</div>
```

### Agrupar secciones

```html
<div>
  <h2>Sección de Noticias</h2>
  <p>Noticia 1...</p>
  <p>Noticia 2...</p>
</div>
```

### Divs con ID y Class

```html
<div id="cabecera">
  <h1>Mi Página</h1>
</div>

<div class="contenido">
  <p>Sección de contenido</p>
</div>

<div id="pie">
  <p>&copy; 2025 - Pie de página</p>
</div>
```

### Maquetar una página completa con Divs

```html
<style>
  #header { background: #ffcccb; padding: 20px; text-align: center; }
  #nav { background: #add8e6; padding: 15px; }
  #main { display: flex; margin: 10px; }
  #content { flex: 3; background: #d3ffd3; padding: 20px; }
  #sidebar { flex: 1; background: #f0e68c; padding: 20px; }
  #footer { background: #ffcccb; padding: 15px; text-align: center; }
</style>

<div id="header">
  <h1>Mi sitio web con DIVs</h1>
</div>

<div id="nav">
  <a href="#">Inicio</a> | <a href="#">Noticias</a> | <a href="#">Contacto</a>
</div>

<div id="main">
  <div id="content">
    <h2>Contenido principal</h2>
    <p>Texto del artículo o información principal.</p>
  </div>
  <div id="sidebar">
    <h3>Barra lateral</h3>
    <p>Enlaces o publicidad.</p>
  </div>
</div>

<div id="footer">
  <p>&copy; 2025 - Mi web de ejemplo</p>
</div>
```

---

## Recursos y referencias

- [HTML Cheat Sheet](https://htmlcheatsheet.com)
- [MDN - Referencia HTML](https://developer.mozilla.org/es/docs/Web/HTML/Reference)
- [W3Schools HTML](https://www.w3schools.com/html/)
- [Ejercicios interactivos W3Schools](https://www.w3schools.com/html/exercise.asp)

**Consejo**: cada vez que aprendas una etiqueta nueva, pruébala en el editor de W3Schools (botón Try it Yourself) y luego intégrala en tu propio proyecto.