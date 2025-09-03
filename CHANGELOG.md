## 2025‑08‑28
### Agregado
- Configuración de `coverage` para medir la cobertura de los tests del proyecto.
- Agregado `requirements.txt` con las dependencias (`coverage`).
- Actualizado `.gitignore` para ignorar carpetas como `htmlcov/` y `venv/`.

### Notas
- El entorno virtual no se incluye en el repositorio.
- Para ejecutar el análisis, usar:

  coverage run -m unittest discover -s . -p "test*.py"
  coverage report -m

  ## 2025-08-28
### Agregado

- Implementación inicial de clase `Dice` con método `tirar()`,que genera dos valores aleatorios entre 1 y 6.
- Test unitario `test_tirar_devuelve_dos_valores` para verificar que se generen correctamente dos valores válidos.

### 2025-08-30
#### Agregado
- Método `resetear()` en clase `Dice`: limpia los valores disponibles al finalizar el turno.
- Método `sin_valores()` en clase `Dice`: indica si ya no quedan valores disponibles.
- Test unitario `test_resetear_limpia_valores` para verificar que se vacía correctamente la lista de dados.
- Test unitario `test_sin_valores_devuelve_true_si_vacio` para verificar el comportamiento esperado antes y después de tirar/resetear.

### 2025-08-31
#### Modificado
- Corregido método `mostrar()` en `Board`
- Agregado test `test_mostrar_no_falla()` para verificar que el método `mostrar()`
- Agregado test `test_obtener_off_color_invalido()` para cubrir el manejo de colores inválidos en `obtener_off()`.

### 2025-08-31
#### Agregado
- Método `interpretar_dados()` en la clase `Tablero` para procesar tiradas de dados.
- Test para verificar el comportamiento con dobles y dados distintos.

### 2025-09-03
#### Agregado
- Clase `Player` con método `obtener_color()` para determinar el color del jugador.
- Tests unitarios `test_color_blanco()` y `test_color_negro()` en `test_player.py`.

### 2025-09-03

#### 🔧 Configuración

- Se implementó **Pylint** para control de calidad del código.
  - Se creó archivo `.pylintrc` con límites personalizados 
- Se actualizó `requirements.txt` para incluir:
  - `pylint` y otras librerías 