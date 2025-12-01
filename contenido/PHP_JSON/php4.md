# Integración

``` mermaid
flowchart LR
  A[Integración cliente-servidor] --> B[Teoría]
  A --> C[Aplicación]

  %% TEORÍA
  B --> B1[API básica con PHP]
  B --> B2[Flujo JS → PHP → JSON → JS]
  B --> B3[Uso de Fetch API]
  B --> B4[Separación Frontend/Backend]

  %% APLICACIÓN
  C --> C1[Crear endpoint PHP con JSON]
  C --> C2[Hacer fetch desde JS]
  C --> C3[Renderizar JSON en el DOM]
  C --> C4[Crear pequeña interfaz dinámica]
```

# 1. ¿Qué es JSON?

JSON (**JavaScript Object Notation**) es un formato de intercambio de datos ligero, universal y fácil de leer.

PHP puede convertir fácilmente estructuras como:

- Arrays indexados → listas JSON  
- Arrays asociativos → objetos JSON  

---

# 2. Convertir PHP a JSON (json_encode)

### Ejemplo con array indexado

```php
<?php
$frutas = ["Manzana", "Pera", "Naranja"];
$json = json_encode($frutas);

echo $json;
// Resultado: ["Manzana","Pera","Naranja"]
?>
```

### Ejemplo con array asociativo

```php
<?php
$persona = [
    "nombre" => "Luis",
    "edad" => 22,
    "ciudad" => "Madrid"
];

echo json_encode($persona);
// {"nombre":"Luis","edad":22,"ciudad":"Madrid"}
?>
```

---

# 3. Convertir JSON a PHP (json_decode)

### De JSON a array asociativo

```php
<?php
$json = '{"nombre":"Ana","edad":20}';
$datos = json_decode($json, true);

echo $datos["nombre"]; // Ana
?>
```

### De JSON a objeto PHP

```php
<?php
$json = '{"nombre":"Ana","edad":20}';
$datos = json_decode($json);

echo $datos->nombre; // Ana
?>
```

---

# 4. Comprobar errores en JSON

```php
<?php
$json = "{nombre: 'Ana'}"; // JSON mal formado
$resultado = json_decode($json);

if ($resultado === null) {
    echo "Error JSON: " . json_last_error_msg();
}
?>
```

---

# 5. Ejemplo completo: generar JSON para JavaScript

Archivo: **datos.php**

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

Salida esperada:

```
{"Laptop":799,"Teclado":25,"Ratón":15}
```

---

# 6. Actividades guiadas

## Actividad 1 — Convertir lista a JSON  
Dado el array:

```php
$colores = ["Rojo", "Verde", "Azul", "Amarillo"];
```

Generar su versión JSON y mostrarla en pantalla.

---

## Actividad 2 — Convertir diccionario a JSON  
Crear un array asociativo que contenga:
- título  
- autor  
- año  

Convertirlo con `json_encode()`.

---

## Actividad 3 — Decodificar JSON  
Dado el JSON:

```json
{"curso":"PHP","nivel":"básico","duracion":10}
```

Transformarlo a array asociativo y mostrar sus valores.

---

# 7. Mini-reto de fin de sesión (adaptado a arrays simples)

Crear un archivo **catalogo.php** que:

1. Declare dos arrays indexados del mismo tamaño:  
   - `$productos = [...]`  
   - `$precios = [...]`  

2. Cree un **array asociativo** combinando ambos, donde la clave sea el nombre del producto y el valor su precio.

   Ejemplo:  
   ```php
   [
     "Laptop" => 799,
     "Teclado" => 25
   ]
   ```

3. Convierta ese array asociativo a JSON.

4. Muestre el resultado final, por ejemplo:

```
{"Laptop":799,"Teclado":25,"Ratón":15}
```

