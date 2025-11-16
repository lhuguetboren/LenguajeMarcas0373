# Práctica: Formulario de Suscripción al Periódico

## 1. Objetivo de la práctica
Crear un formulario de suscripción para **El Diari Digital** utilizando:

- `select`
- `checkbox`
- `option`
- `textarea`
- Validación con JavaScript

## 2. Requisitos del formulario
El formulario, ubicado al final de la página del diario (descargar) debe incluir los siguientes campos:

1. **Nombre completo** 
2. **Correo electrónico**
     - Debe contener `@`
3. **Sexo**
4. **Edad**
5. **Código postal**
6. **Tipo de suscripción** 
>   - Selecciona una opción (vacía)
>  - Básica  
>   - Premium  
>   - Estudiantil
7. **Sección favorita del periódico** 
>   - Actualidad  
>   - Esports  
>   - Cultura  
>   - Tecnologia
8. **Aceptación de condiciones**

9. **Comentario**

10. **Mensaje de envio correcto o con problemas**

## 3. Validación requerida

Al pulsar **“Suscribirme”**:

- Prevenir envío real
- Comprobar:
    - Nombre no vacío
    - Email no vacío y contiene `@`
    - Tipo de suscripción seleccionado
    - Sección seleccionada
    - Checkbox marcado
- Si falla → mensaje en rojo
- Si todo correcto → mensaje en verde
