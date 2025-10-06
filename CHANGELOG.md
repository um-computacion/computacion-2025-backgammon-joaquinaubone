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

## 2025-09-06  
### Agregado

- Implementación de `hay_movimientos_posibles(color, valores_dado)`, función principal que determina si el jugador puede realizar al menos un movimiento válido durante su turno, ya sea desde la barra o desde el tablero.

- Método auxiliar privado `__obtener_direccion(color)`, que devuelve `1` para blancas y `-1` para negras, utilizado para calcular la dirección de movimiento.

- Método auxiliar privado `__calcular_destino_desde_barra(color, valor)`, que calcula la casilla de destino para una ficha que sale de la barra, en base al valor del dado y el color del jugador.

- Método auxiliar privado `__puede_salir_de_barra(color, valores_dado)`, que evalúa si alguna ficha en la barra puede volver al tablero usando los valores de dado actuales.

- Método auxiliar privado `__puede_mover_ficha_en_tablero(color, valores_dado, direccion)`, que determina si alguna ficha en el tablero puede moverse legalmente, incluyendo borneado si corresponde.

## 2025-09-10
### Agregado

- Test `test_movimiento_valido_en_casilla_vacia`: verifica que una casilla vacía sea considerada válida para mover una ficha.
- Test `test_movimiento_valido_misma_ficha`: verifica que una ficha pueda moverse a una casilla ocupada por una ficha del mismo color.
- Test `test_movimiento_valido_una_ficha_oponente`: verifica que se permita mover a una casilla con una sola ficha del rival (golpe).
- Test `test_movimiento_invalido_varias_fichas_oponente`: verifica que no se permita mover a una casilla ocupada por 2 o más fichas del rival.

## 2025-09-10
### Agregado

- Test `test_movimiento_fuera_de_tablero_blanco`: verifica que un destino mayor o igual a 24 sea considerado fuera del tablero para las fichas blancas.
- Test `test_movimiento_fuera_de_tablero_negro`: verifica que un destino menor a 0 sea considerado fuera del tablero para las fichas negras.
- Test `test_movimiento_dentro_de_tablero`: verifica que un destino válido (dentro del rango 0-23) no sea considerado fuera del tablero.

## 2025-09-10
### Agregado

- Test `test_puede_sacar_ficha_false`: verifica que un jugador no puede sacar ficha si aún tiene fichas fuera del último cuarto del tablero.
- Test `test_puede_sacar_ficha_true`: verifica que un jugador pueda sacar ficha si todas sus fichas están en el último cuarto.

- Test `test_gano_blanco`: verifica que el jugador blanco gane cuando tiene 15 fichas borneadas.
- Test `test_gano_negro`: verifica que el jugador negro gane cuando tiene 15 fichas borneadas.
- Test `test_no_gano`: verifica que si no se alcanzan las 15 fichas borneadas, el método `gano()` retorne `False`.

## 2025-09-11
### Agregado

- Test `test_hay_movimiento_posible_desde_tablero`: verifica que existan movimientos posibles para el jugador blanco cuando tiene fichas en el tablero y valores de dado válidos.

- Test `test_hay_movimiento_posible_desde_barra`: simula una ficha en la barra y verifica que se pueda realizar un movimiento desde ahí.

- Test `test_no_hay_movimiento_posible`: asegura que cuando no hay fichas en el tablero ni en la barra, no haya movimientos posibles.

## 2025-09-16
### Agregado

- Test `test_sacar_de_barra_blancas`: verifica que una ficha blanca se retire correctamente de la barra y se calcule bien su destino.
- Test `test_sacar_de_barra_negras`: verifica lo mismo para una ficha negra.
- Test `test_sacar_de_tablero_blancas`: asegura que una ficha blanca se retire correctamente de una casilla del tablero y se calcule el destino.
- Test `test_sacar_de_tablero_negras`: igual que el anterior pero para negras.
- Test `test_sacar_de_tablero_sin_fichas`: verifica que se lance un error si se intenta sacar una ficha de una casilla vacía.
- Test `test_calcular_destino_desde_barra_blanco`: comprueba el cálculo correcto del destino desde barra para blancas.
- Test `test_calcular_destino_desde_barra_negro`: igual que el anterior pero para negras.
- Test `test_obtener_direccion_negro`: asegura que se devuelve `-1` para negras.
- Test `test_obtener_direccion_blanco`: asegura que se devuelve `1` para blancas.
- Test `test_puede_mover_ficha_en_tablero_true`: verifica que se detecte un movimiento posible si lo hay.
- Test `test_puede_mover_ficha_en_tablero_false`: asegura que se devuelve `False` si no hay movimientos posibles.
- Test `test_agregar_a_off_blanco`: comprueba que se agrega una ficha blanca al área de borneadas.
- Test `test_agregar_a_off_negro`: igual que el anterior pero con fichas negras.
- Test `test_mover_color_invalido`: asegura que se lanza un error si se pasa un color inválido.
- Test `test_mover_con_ficha_en_barra_y_origen_distinto_de_cero`: verifica que no se puede mover una ficha del tablero si hay fichas en la barra.
- Test `test_mover_desde_barra_blanca`: prueba que se mueva correctamente una ficha blanca desde la barra.
- Test `test_mover_fuera_de_tablero_sin_poder_bornear`: asegura que se lanza un error si se intenta bornear sin condiciones válidas.
- Test `test_puede_sacar_ficha_inicio_negras`: comprueba que negras no pueden bornear al inicio de la partida.


## 2025-09-16
### Agregado

- Test `test_sacar_de_barra_blancas`: verifica que una ficha blanca se retire correctamente de la barra y se calcule bien su destino.
- Test `test_sacar_de_barra_negras`: verifica lo mismo para una ficha negra.
- Test `test_sacar_de_tablero_blancas`: asegura que una ficha blanca se retire correctamente de una casilla del tablero y se calcule el destino.
- Test `test_sacar_de_tablero_negras`: igual que el anterior pero para negras.
- Test `test_sacar_de_tablero_sin_fichas`: verifica que se lance un error si se intenta sacar una ficha de una casilla vacía.
- Test `test_calcular_destino_desde_barra_blanco`: comprueba el cálculo correcto del destino desde barra para blancas.
- Test `test_calcular_destino_desde_barra_negro`: igual que el anterior pero para negras.
- Test `test_obtener_direccion_negro`: asegura que se devuelve `-1` para negras.
- Test `test_obtener_direccion_blanco`: asegura que se devuelve `1` para blancas.
- Test `test_puede_mover_ficha_en_tablero_true`: verifica que se detecte un movimiento posible si lo hay.
- Test `test_puede_mover_ficha_en_tablero_false`: asegura que se devuelve `False` si no hay movimientos posibles.
- Test `test_agregar_a_off_blanco`: comprueba que se agrega una ficha blanca al área de borneadas.
- Test `test_agregar_a_off_negro`: igual que el anterior pero con fichas negras.
- Test `test_mover_color_invalido`: asegura que se lanza un error si se pasa un color inválido.
- Test `test_mover_con_ficha_en_barra_y_origen_distinto_de_cero`: verifica que no se puede mover una ficha del tablero si hay fichas en la barra.
- Test `test_mover_desde_barra_blanca`: prueba que se mueva correctamente una ficha blanca desde la barra.
- Test `test_mover_fuera_de_tablero_sin_poder_bornear`: asegura que se lanza un error si se intenta bornear sin condiciones válidas.
- Test `test_puede_sacar_ficha_inicio_negras`: comprueba que negras no pueden bornear al inicio de la partida.

## 2025-09-17
### Agregado

- Clase `Juego` que representa el controlador principal del juego.
- Método `__init__`: inicializa el juego con el tablero, dados y jugadores.
- Método `obtener_jugador_actual`: devuelve el jugador correspondiente al turno actual.
- Método `verificar_fin_del_juego`: determina si el jugador actual ha ganado.
- Método `hay_movimientos_disponibles`: verifica si hay jugadas posibles con la tirada actual.

## 2025-09-17
### Agregado

- Método `intentar_jugada`: permite ejecutar un movimiento desde una posición con determinada cantidad de pasos para el jugador actual. Lanza excepción si no es válido.
- Método `interpretar_tirada`: interpreta una tirada de dados usando la lógica de la clase `Tablero`, devolviendo una lista de valores (doble o normal).

## 2025-09-18
### Agregado

- Test `test_obtener_jugador_actual`: verifica que se obtenga correctamente el jugador correspondiente al turno actual.
- Test `test_verificar_fin_del_juego_false`: comprueba que el juego no ha finalizado cuando aún ningún jugador ha ganado

## 2025-09-18
### Agregado

- Test `test_hay_movimientos_disponibles_true`: verifica que se detecten movimientos disponibles cuando hay jugadas posibles.
- Test `test_interpretar_tirada_no_doble`: verifica que una tirada normal (sin dobles) se interprete correctamente.
- Test `test_interpretar_tirada_doble`: verifica que una tirada doble genere cuatro valores iguales.

## 2025-09-19
### Agregado

- Test `test_intentar_jugada_valida`: verifica que una jugada válida mueve correctamente una ficha en el tablero.
- Test `test_intentar_jugada_invalida`: verifica que se lance un `ValueError` al intentar una jugada inválida (por ejemplo, movimiento que no corresponde al turno actual).

## 2025-09-23
### Agregado

- Archivo `main.py` con función `main()` para inicializar el juego.  
- Creación de instancias de:
  - `Tablero` con configuración inicial (`setup()`),
  - `Dice` para gestionar los dados,
  - `Player` para jugadores blanco y negro.  
- Preparación del punto de entrada `if __name__ == '__main__':` para ejecutar el juego desde consola.

## 2025-09-24
### Agregado
- Archivo `cli.py` que maneja la interacción con el usuario.
- Función `jugar`: inicializa el bucle principal del juego desde la interfaz de línea de comandos.
  - Muestra de quién es el turno actual.
  - Tira los dados y muestra el resultado.
  - Verifica si hay movimientos posibles; en caso contrario, pasa el turno.

## 2025-09-25
### Agregado
- Manejo de jugadas dentro de un turno en la CLI:
  - Muestra el estado actual del tablero y los valores de la tirada.
  - Solicita al usuario la casilla de origen y los pasos a mover.
  - Valida que el valor de los pasos esté en la tirada disponible.
  - Fuerza mover fichas desde la barra si existen.
  - Ejecuta la jugada en el tablero y actualiza la tirada.
  - Maneja errores mediante `try/except`, mostrando mensajes claros al usuario.

## 2025-09-25
### Agregado
- CLI: finalización del turno y del juego.
  - Verifica si el jugador actual ganó luego de completar sus jugadas.
  - Si no ganó, cambia el turno al otro jugador.
  - Muestra en pantalla un mensaje de victoria cuando el jugador gana la partida.

## 2025-09-26
### Agregado

- Función `jugar(tablero, dados, jugador_blanco, jugador_negro)` en `cli.py`: gestiona el bucle principal del juego, mostrando el estado del tablero, turnos de los jugadores, tiradas de dados y controlando el flujo de la partida hasta determinar un ganador.

## 2025-09-26
### Corregido
- Se resolvieron conflictos en `CHANGELOG.md` ocasionados por un merge.
- Se unificaron entradas duplicadas y se eliminó sintaxis conflictiva 

## 2025-09-27
### Agregado
- Workflow `cli.yml` en `.github/workflows/` para generar reportes automáticos.  
- Ejecución de tests con `coverage` y exportación en formatos `xml` y `txt`.  
- Ejecución de `pylint` con configuración desde `.pylintrc` y guardado de reporte.  
- Script automático `generate_reports.py` que combina los resultados en `REPORTS.md`.  
- Pull request automático con los reportes actualizados al branch `main`.  

## 2025-09-30
### Configuración

- Se agregó archivo `.coveragerc` para personalizar la ejecución de Coverage.
- Se configuró la opción `[run].omit` para excluir todos los archivos de tests (`test_*.py` y `tests/*`) de los reportes de cobertura.

## 2025-10-01
### Modificado
- Reemplazados los tests antiguos del método `tirar()` en la clase `Dice` por una nueva versión que usa `@patch` para controlar el comportamiento de `random.randint`.  
- Agregado el test `test_tirar_devuelve_dos_valores` que valida correctamente que:
  - Se generen dos valores de dado.  
  - Los valores devueltos coincidan con lo simulado (ejemplo: `[5,2]`).  
  - `random.randint` sea llamado exactamente dos veces.  

  ## 2025-10-02
### Modificado
- Se corrigió el formato de `Dice/dice.py` eliminando espacios sobrantes al final de línea.
- Se agregó nueva línea final al archivo para cumplir con las reglas de `pylint`.
- Se añadieron docstrings a la clase y métodos de `Dice` para mejorar la legibilidad y el puntaje de análisis estático.

## 2025-10-04
### Modificado

- Se corrigieron advertencias de formato en `test_dice.py` detectadas por *Pylint*:
  - Eliminación de espacios en blanco al final de línea (C0303).
  - Agregado salto de línea final (C0304).
- No se realizaron cambios funcionales: solo mejoras de estilo y cumplimiento de PEP8.

## 2025-10-05
### Modificado

- Renombrada la carpeta `Checker` a `checker` para cumplir con las convenciones de nomenclatura de PEP 8.
- Actualizados los `import` en todo el proyecto:
  - De `from Checker.checker import Checker` → a `from checker.checker import Checker`.
- Mejora en la legibilidad y consistencia del código según las normas de Pylint.

## 2025-10-06
### Corregido
- Se agregó una línea en blanco al final del archivo `checker/test_checker.py` para cumplir con la regla **C0304 (missing-final-newline)** de Pylint.
