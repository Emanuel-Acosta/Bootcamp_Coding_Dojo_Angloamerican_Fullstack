# Patrones de validación
## Validación de email
 `r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$' `
### **Explicación**:

1. **`^`**:
    - Indica el **inicio** de la cadena.
    - Asegura que el patrón comience desde el principio del texto.
2. **`[a-zA-Z0-9.+_-]+`**:
    
    - Coincide con uno o más (`+`) de los siguientes caracteres:
        - Letras mayúsculas (`A-Z`).
        - Letras minúsculas (`a-z`).
        - Dígitos (`0-9`).
        - Los caracteres permitidos adicionales: punto (`.`), signo más (`+`), guion bajo (`_`), y guion medio (`-`).
    - Representa el **nombre de usuario** del correo electrónico (antes del `@`).
3. **`@`**:
    
    - Coincide con el símbolo `@`.
    - Es obligatorio y separa el nombre de usuario del dominio.
4. **`[a-zA-Z0-9._-]+`**:
    
    - Coincide con uno o más (`+`) de los siguientes caracteres:
        - Letras (`a-z`, `A-Z`).
        - Dígitos (`0-9`).
        - Punto (`.`), guion bajo (`_`), o guion medio (`-`).
    - Representa la **parte del dominio** (por ejemplo, `gmail`, `outlook`, `empresa`).
5. **`\.`**:
    
    - Escapa el carácter punto (`.`), asegurando que actúe como un literal.
    - Se utiliza para separar la parte principal del dominio de su extensión (por ejemplo, el `.` en `.com` o `.org`).
6. **`[a-zA-Z]+`**:
    
    - Coincide con una o más (`+`) letras (`a-z`, `A-Z`).
    - Representa la **extensión del dominio** (por ejemplo, `com`, `org`, `edu`).
7. **`$`**:
    
    - Indica el **final** de la cadena.
    - Asegura que no haya caracteres adicionales después del dominio.

---

### **Ejemplo de correos válidos**:

- `user@example.com`
- `nombre.apellido@gmail.com`
- `usuario+alias@empresa.co`
- `test_user-123@subdominio.example.org`

### **Ejemplo de correos inválidos**:

1. **Sin el `@`**:
    - `usernameexample.com`
2. **Con caracteres no permitidos**:
    - `user!name@example.com` (el `!` no es válido).
3. **Falta extensión del dominio**:
    - `user@domain.` o `user@domain`
4. **Espacios**:
    - `user @example.com` (los espacios no son válidos).