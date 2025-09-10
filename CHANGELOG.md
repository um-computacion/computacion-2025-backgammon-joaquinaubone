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

#### Configuración

- Se implementó **Pylint** para control de calidad del código.
  - Se creó archivo `.pylintrc` con límites personalizados 
- Se actualizó `requirements.txt` para incluir:
  - `pylint` y otras librerías 

  ### 2025-09-04

#### Funcionalidad nueva

- Se agregó la clase `Ficha` para representar una ficha del juego de Backgammon.
  - Atributo: `color`
  - Métodos:
    - `obtener_color()`: retorna el color de la ficha.
- Se agregó el archivo `test_ficha.py` con tests unitarios que verifican:
  - La creación de fichas blancas y negras.
  - La correcta obtención del color.

  ## 2025-09-04 
  ## agregado

	-  Se implementa el método para alternar entre los turnos 'B' (blancas) y 'N' (negras).
	-  Se agrega test unitario para verificar el correcto funcionamiento del cambio de turno.

  ## 2025-09-05
  ### Agregado

- `__es_movimiento_fuera_de_tablero(color, destino)`: función auxiliar que verifica si el movimiento propuesto sale del tablero según el color del jugador.

- `puede_sacar_ficha(color)`: nueva función que determina si el jugador tiene todas sus fichas en el ultimo cuarto y, por lo tanto, puede comenzar a sacar fichas.

- `gano(color)`: función que verifica si el jugador ya saco las 15 fichas y, por lo tanto, ganó la partida.

## 2025-09-07
## agregado

	- test_es_movimiento_valido_*: Verifican la validez de distintos estados de una casilla destino.
	- test_es_movimiento_fuera_de_tablero_*: Evalúan si el destino está fuera del rango permitido según el color.
	- test_puede_sacar_ficha_true / false: Comprueban si un jugador puede comenzar a sacar fichas (bornear).
	- test_gano_true / false: Verifican la condición de victoria para blancos y negros.

## 2025-09-06
### Agregado

- `mover(origen, pasos, color)`: función principal para ejecutar un movimiento de una ficha desde una posición de origen (o la barra) hacia una posición de destino, manejando golpes, borneado y validaciones de reglas.

- `__sacar_de_barra(color, pasos)`: función auxiliar que remueve una ficha desde la barra correspondiente y calcula el destino según el color y valor del dado.

- `__sacar_de_tablero(origen, pasos, color)`: función auxiliar que remueve una ficha desde el tablero, validando que el origen pertenezca al jugador y calculando su destino según el color.

- `__agregar_a_off(color, ficha)`: función auxiliar para agregar una ficha a la zona de borneado del color correspondiente.

- `__mover_a_destino(destino, ficha, color)`: función auxiliar que maneja el movimiento a la casilla de destino, incluyendo validación de casillas ocupadas y envío al bar en caso de golpe.