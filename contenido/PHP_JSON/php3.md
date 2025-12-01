# Arrays Asociativos + JSON


``` mermaid
flowchart LR
  A[Arrays asociativos + JSON] --> B[Teoría]
  A --> C[Aplicación]

  %% TEORÍA
  B --> B1[Arrays asociativos]
  B --> B2[Arrays multidimensionales]
  B --> B3[JSON como formato estándar]
  B --> B4[json_encode / json_decode]

  %% APLICACIÓN
  C --> C1[Crear arrays tipo diccionario]
  C --> C2[Convertir a JSON]
  C --> C3[Leer JSON y acceder a campos]
  C --> C4[Usar JSON en estructuras complejas]
```

# 1. ¿Qué es un array en PHP?

Un **array** es una estructura que permite almacenar múltiples valores dentro de una sola variable.

PHP permite:
- Arrays **indexados** (con índices numéricos)
- Arrays **asociativos** (clave → valor)

---

# 2. Arrays indexados

Son arrays cuyos elementos se identifican mediante índices numéricos.

```php
<?php
$frutas = ["Manzana", "Pera", "Naranja"];
echo $frutas[0]; // Manzana
?>
```

Agregar un nuevo valor:

```php
$frutas[] = "Kiwi";
```

Modificar un valor existente:

```php
$frutas[1] = "Plátano"; // Reemplaza "Pera"
```

---

# 3. Arrays asociativos

Son arrays donde se usa una **clave** para identificar cada valor.

```php
<?php
$persona = [
    "nombre" => "Ana",
    "edad"   => 20,
    "ciudad" => "Barcelona"
];

echo $persona["nombre"]; // Ana
?>
```

Agregar un nuevo par clave–valor:

```php
$persona["pais"] = "España";
```

---

# 4. Recorrido de arrays

## 4.1. Con `for` (solo arrays indexados)

```php
<?php
$frutas = ["Manzana", "Plátano", "Naranja"];

for ($i = 0; $i < count($frutas); $i++) {
    echo $frutas[$i] . "<br>";
}
?>
```

## 4.2. Con `foreach` (indexados o asociativos)

### Indexados:

```php
foreach ($frutas as $fruta) {
    echo $fruta . "<br>";
}
```

### Asociativos:

```php
foreach ($persona as $clave => $valor) {
    echo $clave . ": " . $valor . "<br>";
}
```

---

# 5. Ejemplo integrado: tabla HTML generada desde un array simple

```php
<?php
$productos = [
    "Laptop" => 799,
    "Teclado" => 25,
    "Ratón" => 15
];
?>

<table border="1">
    <tr>
        <th>Producto</th>
        <th>Precio (€)</th>
    </tr>

    <?php foreach ($productos as $nombre => $precio): ?>
    <tr>
        <td><?php echo $nombre; ?></td>
        <td><?php echo $precio; ?></td>
    </tr>
    <?php endforeach; ?>
</table>
```

---

# 6. Actividades guiadas

## Actividad 1 — Lista de colores
Crear un array indexado con 5 colores y mostrarlos usando `foreach`.

---

## Actividad 2 — Diccionario de usuario
Crear un array asociativo con:
- nombre  
- edad  
- correo  
- país  

Mostrarlo en formato HTML.

---

# 7. Mini‑reto de fin de sesión (versión modificada)

Crear un archivo **inventario.php** que:

1. Use **dos arrays simples**:
   - Uno con nombres de productos (indexado)
   - Otro con precios (indexado y con el mismo número de elementos)

   Ejemplo:
   ```php
   $productos = ["Laptop", "Teclado", "Ratón"];
   $precios = [799, 25, 15];
   ```

2. Recorra ambos arrays al mismo tiempo usando `for` y muestre:
   ```
   Producto X — Precio: Y €
   ```

3. Calcule el precio total del inventario sumando todos los precios.

Debe utilizar:
- Arrays indexados  
- Recorridos `for`  
- Operadores aritméticos  

---

# 8. Resultado esperado

Al final de esta sesión, el estudiante será capaz de:
- Crear y usar arrays indexados y asociativos.
- Recorrer arrays usando `for` y `foreach`.
- Representar datos simples en estructuras adecuadas.
- Preparar los datos para su conversión a JSON en la siguiente sesión.

