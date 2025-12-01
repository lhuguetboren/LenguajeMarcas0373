# Variables y Arrays simples

``` mermaid
flowchart LR
  A[Variables y arrays] --> B[Teoría]
  A --> C[Aplicación]

  %% TEORÍA
  B --> B1[Variables y tipado dinámico]
  B --> B2[Tipos básicos]
  B --> B3[Operadores y concatenación]
  B --> B4[Arrays indexados]

  %% APLICACIÓN
  C --> C1[Declarar e imprimir variables]
  C --> C2[Realizar operaciones]
  C --> C3[Crear arrays y recorrerlos]
  C --> C4[Generar listas HTML desde PHP]
```

# 1. Variables en PHP

En PHP, todas las variables comienzan con el símbolo **`$`**.

```php
<?php
$nombre = "Ana";
$edad = 21;
?>
```

Reglas básicas:

- Deben comenzar con `$`.
- No pueden iniciar con números.
- Son *case-sensitive* (`$Nombre` ≠ `$nombre`).
- PHP es de tipado dinámico: el tipo depende del valor asignado.

---

# 2. Tipos de datos en PHP

### Tipos básicos más comunes
- **String** — textos  
- **Integer** — enteros  
- **Float** — decimales  
- **Boolean** — `true` o `false`

Ejemplo:

```php
<?php
$texto = "Hola";
$numero = 42;
$precio = 10.5;
$activo = true;
?>
```

---

# 3. Concatenación en PHP

PHP utiliza el operador **`.`** para concatenar textos.

```php
<?php
$nombre = "Ana";
echo "Hola " . $nombre;
?>
```

También se puede concatenar con valores numéricos:

```php
<?php
$precio = 15;
echo "Total: €" . $precio;
?>
```

---

# 4. Operadores aritméticos

| Operador | Descripción  | Ejemplo |
|----------|--------------|---------|
| `+` | Suma | `$a + $b` |
| `-` | Resta | `$a - $b` |
| `*` | Multiplicación | `$a * $b` |
| `/` | División | `$a / $b` |
| `%` | Módulo | `$a % $b` |

Ejemplo:

```php
<?php
$a = 10;
$b = 3;
echo $a + $b; // 13
echo $a % $b; // 1
?>
```

---

# 5. Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `==` | Igualdad |
| `!=` | Diferente |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

Ejemplo:

```php
<?php
$edad = 18;
echo ($edad >= 18); // true (1)
?>
```

---

# 6. Operadores lógicos

| Operador | Significado |
|----------|-------------|
| `&&` | AND |
| `||` | OR |
| `!` | NOT |

Ejemplo:

```php
<?php
$edad = 20;
$activo = true;
echo ($edad > 18 && $activo); // true
?>
```

---

# 7. Ejemplo integrado

```php
<?php
$nombre = "Luis";
$productos = 4;
$precioUnitario = 5.5;

$total = $productos * $precioUnitario;

echo "Cliente: " . $nombre . "<br>";
echo "Total a pagar: €" . $total;
?>
```

---

# 8. Actividades guiadas

## Actividad 1 — Ficha personal

Crear un archivo `ficha.php` con:
- Nombre  
- Edad  
- Ciudad  
- Mensaje final concatenado

Ejemplo esperado:

```
Nombre: Carla  
Edad: 22  
Ciudad: Barcelona  
Hola Carla, vives en Barcelona.
```

---

## Actividad 2 — Calculadora básica
Solicitar dos números dentro del código y mostrar:
- Suma  
- Resta  
- Multiplicación  
- División  

---

## Actividad 3 — Validación simple
Crear una variable `$nota` y mostrar:
- “Aprobado” si es mayor o igual a 5  
- “Suspendido” si es menor a 5  

---

# 9. Mini-reto de fin de sesión

Crear un archivo `carrito.php` que contenga:
- Nombre del cliente  
- Tres productos con precios  
- Cálculo total  
- Un mensaje: `El total de la compra de X es Y euros.`

Debe usar:

- Variables  
- Operadores aritméticos  
- Concatenación  
