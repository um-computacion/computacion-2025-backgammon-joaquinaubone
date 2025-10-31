# JUSTIFICACION.md - Proyecto Backgammon

## 1. Resumen del Diseño General

El proyecto implementa un juego de Backgammon en Python siguiendo una **arquitectura modular** que separa completamente la lógica de negocio de las interfaces de usuario. Esta separación permite tener múltiples frontends (CLI y Pygame) utilizando el mismo núcleo de lógica del juego.

### Arquitectura del Sistema

```
/backgammon/
├── core/           → Lógica pura del juego (independiente de UI)
│   ├── checker.py
│   ├── player.py
│   ├── dice.py
│   ├── board.py
│   ├── game.py
│   └── exceptions.py
├── cli/            → Interfaz de línea de comandos
│   └── cli.py
├── pygameUI/       → Interfaz gráfica
│   └── pygame_ui.py
├── tests/          → Pruebas unitarias
│   ├── test_checker.py
│   ├── test_player.py
│   ├── test_dice.py
│   ├── test_board.py
│   ├── test_game.py
│   └── test_cli.py
└── main.py         → Punto de entrada
```

**Principio fundamental:** El módulo `core/` no tiene dependencias de `cli/` ni `pygameUI/`. Las interfaces dependen del core, nunca al revés.

---

## 2. Justificación de las Clases Elegidas

### 2.1. Clase `Checker` (core/checker.py)

**Responsabilidad:** Representar una ficha individual del juego.

**Justificación:** 
- En Backgammon, cada ficha es una entidad con identidad propia (color).
- Siguiendo el principio de **Single Responsibility**, Checker solo se encarga de mantener el color de la ficha y proporcionar su representación visual.
- Es la unidad atómica del juego.

**Métodos:**
- `obtener_color()`: Retorna el color de la ficha
- `__str__()`: Representación visual (X para blancas, O para negras)
- `__repr__()`: Representación técnica para debugging

### 2.2. Clase `Player` (core/player.py)

**Responsabilidad:** Representar a un jugador del juego.

**Justificación:**
- Encapsula la información del jugador (color).
- Proporciona métodos para obtener representación del jugador.
- Permite extensión futura (nombre, estadísticas, IA, etc.) sin modificar otras clases (Open/Closed Principle).

**Métodos:**
- `obtener_color()`: Retorna el color del jugador
- `obtener_simbolo()`: Retorna el símbolo visual que usa el jugador

### 2.3. Clase `Dice` (core/dice.py)

**Responsabilidad:** Gestionar las tiradas de dados.

**Justificación:**
- Los dados son un componente crítico del juego con lógica específica (dobles permiten 4 movimientos).
- Centralizar la lógica de dados facilita el testing (inyección de valores fijos en tests).
- Permite cambiar la fuente de aleatoriedad sin afectar otras clases.

**Métodos:**
- `tirar()`: Genera una nueva tirada de dados
- `obtener_valores()`: Retorna los valores actuales de los dados

### 2.4. Clase `Board` (core/board.py)

**Responsabilidad:** Gestionar el estado completo del tablero de juego.

**Justificación:**
- Es el **Single Source of Truth** del estado del juego.
- Encapsula toda la complejidad de movimientos, capturas, barra y fichas fuera.
- Siguiendo SRP, Board no decide quién juega o cuándo termina el juego, solo mantiene y modifica el estado.

**Atributos principales:**
- `__points__`: Lista de 24 posiciones (listas de Checkers)
- `__bar__`: Diccionario con fichas capturadas {'B': [], 'N': []}
- `__off__`: Diccionario con fichas sacadas {'B': [], 'N': []}

**Métodos principales:**
- `setup()`: Inicializa el tablero con configuración estándar
- `get_point(posicion)`: Obtiene las fichas en una posición
- `mover(origen, destino, color)`: Mueve una ficha validando reglas
- `capturar(posicion, color)`: Captura ficha enemiga y la envía a barra
- `sacar(posicion, color)`: Saca una ficha del tablero (bear off)
- `mostrar()`: Renderiza el tablero en consola
- Métodos de validación: `puede_mover()`, `puede_capturar()`, `puede_sacar_ficha()`

### 2.5. Clase `Game` (core/game.py)

**Responsabilidad:** Coordinar el flujo del juego y aplicar las reglas de Backgammon.

**Justificación:**
- Actúa como **coordinador** entre Board, Dice y Players.
- Implementa las reglas de alto nivel del juego (turnos, condiciones de victoria, validaciones de movimientos).
- Permite separar "qué se puede hacer" (Game) de "cómo se visualiza" (CLI/Pygame).

**Atributos principales:**
- `tablero`: Instancia de Board
- `dados`: Instancia de Dice
- `jugadores`: Diccionario {'B': Player, 'N': Player}
- `turno_actual`: Color del jugador en turno

**Métodos principales:**
- `mover(origen, pasos)`: Ejecuta un movimiento validando todas las reglas
- `gano()`: Verifica si el jugador actual ganó
- `hay_movimientos_posibles(color, valores_dado)`: Verifica si hay jugadas legales
- `puede_sacar_ficha(color)`: Verifica si el jugador puede hacer bear off
- `cambiar_turno()`: Alterna entre jugadores

### 2.6. Módulo `exceptions.py` (core/exceptions.py)

**Responsabilidad:** Definir excepciones personalizadas del dominio.

**Justificación:**
- Proporciona claridad semántica a los errores del juego.
- Facilita el manejo diferenciado de errores por tipo.
- Sigue el principio de **Interface Segregation** al tener excepciones específicas.

**Excepciones definidas:**
- `BackgammonException`: Excepción base
- `PosNoExistenteException`: Posición fuera del rango [1-24]
- `ColorInvalidoException`: Color no es 'B' ni 'N'
- `PosicionInvalida`: Posición inválida para movimiento específico

### 2.7. Clase `CLI` (cli/cli.py)

**Responsabilidad:** Proporcionar interfaz de texto para jugar.

**Justificación:**
- Implementa el requisito obligatorio de interfaz de línea de comandos.
- Solo se encarga de I/O y presentación, delegando toda lógica a Game.
- Permite jugar en entornos sin interfaz gráfica.

**Métodos principales:**
- `jugar()`: Loop principal del juego en consola
- `solicitar_movimiento()`: Pide input al usuario
- `mostrar_estado()`: Muestra tablero y dados

### 2.8. Clase `PygameUI` (pygameUI/pygame_ui.py)

**Responsabilidad:** Proporcionar interfaz gráfica para jugar.

**Justificación:**
- Implementa el requisito obligatorio de interfaz con Pygame.
- Reutiliza completamente la lógica de Game.
- Proporciona experiencia visual mejorada.

**Métodos principales:**
- `run()`: Loop principal con eventos de Pygame
- `draw_board()`: Renderiza el tablero gráficamente
- `handle_click()`: Procesa clicks del mouse

---

## 3. Justificación de Atributos

### 3.1. Por qué todos los atributos usan `__nombre__`

**Decisión:** Todos los atributos de instancia se definen con doble guion bajo antes y después del nombre (ej: `__color__`, `__points__`).

**Justificación:**
- **Requisito explícito de la consigna:** "Todos los atributos de todas las clases deben contener como prefijo y postfijo los símbolos '__'".
- **Encapsulamiento fuerte:** Python mangling hace que los atributos sean más difíciles de acceder accidentalmente desde fuera de la clase.
- **Consistencia:** Aplicar la regla uniformemente en todo el proyecto facilita el mantenimiento.

**Nota:** Aunque en Python puro se prefiere `_nombre` (un guion bajo) para atributos privados, seguimos la convención establecida en la consigna del proyecto.

### 3.2. Atributos de `Board`

**`__points__` (lista de listas):**
- Representa las 24 posiciones del tablero.
- Cada posición es una lista de objetos Checker.
- Lista vacía significa posición sin fichas.

**`__bar__` (diccionario):**
- Almacena fichas capturadas por color: `{'B': [], 'N': []}`.
- Diccionario porque cada color tiene su propia barra.

**`__off__` (diccionario):**
- Almacena fichas sacadas del tablero por color: `{'B': [], 'N': []}`.
- Diccionario para mantener el conteo de fichas fuera por cada jugador.

**Alternativas consideradas y descartadas:**
- Usar diccionario para `__points__`: Rechazado porque índices numéricos [0-23] son más naturales.
- Usar clases separadas para Bar y Off: Rechazado por simplicidad, diccionarios son suficientes.

### 3.3. Atributos de `Game`

**`tablero`, `dados`, `jugadores`:**
- **Dependency Injection:** Game recibe estos objetos en `__init__` en lugar de crearlos internamente.
- **Ventajas:**
  - Facilita testing (inyectar mocks).
  - Mayor flexibilidad (cambiar implementaciones).
  - Sigue Dependency Inversion Principle.

**`turno_actual` (string 'B' o 'N'):**
- Almacena el color del jugador en turno.
- Simple y suficiente, no requiere objeto complejo.

---

## 4. Decisiones de Diseño Relevantes

### 4.1. Board como Single Source of Truth (SSoT)

**Decisión:** El objeto Board mantiene TODO el estado del juego. Game nunca mantiene estado duplicado.

**Justificación:**
- Evita inconsistencias (una sola fuente de verdad).
- Facilita serialización futura (guardar/cargar partidas).
- Simplifica debugging (un solo lugar donde inspeccionar estado).

**Implementación:**
- Game consulta a Board para toda información de estado.
- Game nunca cachea información del tablero.

### 4.2. Separación Core/UI (Arquitectura en Capas)

**Decisión:** Lógica del juego completamente independiente de interfaces.

**Justificación:**
- **Testabilidad:** Core se testea sin necesidad de UI.
- **Reutilización:** Múltiples UIs usan el mismo core.
- **Mantenibilidad:** Cambios en UI no afectan lógica y viceversa.
- **Extensibilidad:** Agregar nueva UI (web, mobile) sin tocar core.

**Implementación:**
- Core no importa cli ni pygameUI.
- CLI y PygameUI importan y usan Game.

### 4.3. Validaciones en Board vs Game

**Decisión:** Board valida operaciones físicas, Game valida reglas de juego.

**Justificación:**
- **Separation of Concerns:**
  - Board: "¿puedo poner una ficha aquí físicamente?"
  - Game: "¿es legal este movimiento según las reglas?"
- **Reutilización:** Board puede usarse en variantes de Backgammon.

Board valida operaciones físicas (¿existe la posición?, ¿hay fichas?), mientras que Game valida reglas de juego (¿coincide con dados?, ¿hay fichas en barra?).

### 4.4. Uso de Excepciones para Control de Flujo

**Decisión:** Usar excepciones personalizadas para errores de validación.

**Justificación:**
- **Claridad:** `PosNoExistenteException` es más claro que `ValueError("posición inválida")`.
- **Granularidad:** Permite capturar errores específicos con except.
- **Pythonic:** En Python, "Easier to Ask Forgiveness than Permission" (EAFP) es idiomático.

**Implementación:**
- Todas las excepciones heredan de `BackgammonException`.
- Permite capturar cualquier error del juego con `except BackgammonException`.

### 4.5. Representación Visual en Checker vs CLI

**Decisión:** Checker tiene `__str__()` que retorna su símbolo (X/O), CLI lo usa para mostrar.

**Justificación:**
- Checker conoce su representación básica (SRP).
- CLI puede usar esa representación o agregar colores/formato.
- Facilita testing: `str(checker)` retorna valor predecible.


---

## 5. Excepciones y Manejo de Errores

### 5.1. Jerarquía de Excepciones

```
BackgammonException (base)
├── PosNoExistenteException
├── ColorInvalidoException
└── PosicionInvalida
```

### 5.2. Descripción de cada excepción

**`BackgammonException`:**
- Excepción base para todo error del dominio.
- Permite capturar cualquier error del juego con un único `except`.

**`PosNoExistenteException`:**
- Se lanza cuando se intenta acceder a posición fuera del rango [1-24].
- Ejemplo: `board.get_point(30)` lanza esta excepción.

**`ColorInvalidoException`:**
- Se lanza cuando se usa un color que no es 'B' ni 'N'.
- Ejemplo: `Player('R')` lanza esta excepción.

**`PosicionInvalida`:**
- Se lanza cuando una operación usa posición inválida en contexto específico.
- Ejemplo: intentar mover desde posición sin fichas del color actual.

### 5.3. Estrategia de Manejo de Errores

**En Core:**
- Métodos lanzan excepciones cuando detectan errores.
- No se capturan internamente (excepto cuando es parte de la lógica).
- Validaciones antes de modificar estado.

**En CLI:**
- Captura excepciones de Game/Board.
- Muestra mensaje amigable al usuario.
- Permite reintentar la operación.

**En Pygame:**
- Captura excepciones al procesar clicks.
- Muestra feedback visual.
- No interrumpe el loop del juego.

### 5.4. Validaciones Preventivas

Además de excepciones, se usan métodos de validación antes de intentar operaciones, evitando lanzar excepciones innecesarias y permitiendo a la UI deshabilitar opciones inválidas proactivamente.

---

## 6. Estrategias de Testing y Cobertura

### 6.1. Framework Utilizado

**unittest:** Framework estándar de Python para testing.

**Justificación:**
- No requiere instalación adicional.
- Suficientemente potente para las necesidades del proyecto.
- Integración nativa con `coverage.py`.

### 6.2. Estructura de Tests

```
tests/
├── test_checker.py   → Tests de Checker
├── test_player.py    → Tests de Player
├── test_dice.py      → Tests de Dice
├── test_board.py     → Tests de Board (más exhaustivo)
├── test_game.py      → Tests de Game (reglas de alto nivel)
└── test_cli.py       → Tests de CLI (con mocks)
```


### 6.5. Cobertura de Código

**Objetivo:** >90% de cobertura en módulo core.

**Medición:**
```bash
coverage run -m unittest discover tests/
coverage report
```


---

## 7. Referencias a Requisitos SOLID y Cómo se Cumplen

### 7.1. Single Responsibility Principle (SRP)

**Definición:** Cada clase debe tener una única razón para cambiar.

**Cumplimiento:**
- **Checker:** Solo responsable de representar una ficha.
- **Player:** Solo responsable de representar un jugador.
- **Dice:** Solo responsable de generar tiradas.
- **Board:** Solo responsable de mantener estado del tablero.
- **Game:** Solo responsable de coordinar flujo y aplicar reglas.
- **CLI/Pygame:** Solo responsables de presentación e input.

**Ejemplo:** Si cambian las reglas de movimiento, solo Game cambia. Si cambia la representación visual, solo CLI/Pygame cambian.

### 7.2. Open/Closed Principle (OCP)

**Definición:** Clases abiertas a extensión, cerradas a modificación.

**Cumplimiento:**
- Se agregó Pygame sin modificar core.
- Se pueden agregar nuevas excepciones sin modificar clases existentes.
- Posible agregar IA o nueva UI sin tocar código existente.

### 7.3. Liskov Substitution Principle (LSP)

**Definición:** Objetos de subclases deben poder reemplazar objetos de superclase.

**Cumplimiento:**
- Todas las excepciones custom heredan de `BackgammonException`.
- Cualquier lugar que capture `BackgammonException` funciona con sus subclases sin romper contratos.

### 7.4. Interface Segregation Principle (ISP)

**Definición:** Clientes no deben depender de interfaces que no usan.

**Cumplimiento:**
- Excepciones específicas permiten capturar solo errores relevantes.
- Métodos focalizados en Board (`mover`, `capturar`, `sacar`) en lugar de método genérico.

### 7.5. Dependency Inversion Principle (DIP)

**Definición:** Módulos de alto nivel no deben depender de módulos de bajo nivel.

**Cumplimiento:**
- Game recibe tablero, dados y jugadores en `__init__` (Dependency Injection).
- Core no importa cli ni pygameUI, solo ellos dependen del core.
- Permite inyectar mocks en tests y cambiar implementaciones fácilmente.

---

## 8. Anexos

## 8.1 Diagrama de clases UML
┌─────────────────────────────────────────────────────────────────────────────┐
│                           EXCEPCIONES                                        │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────────────┐
                    │  BackgammonException         │
                    │  <<exception>>               │
                    └──────────────┬───────────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  │                │                │
         ┌────────▼──────┐  ┌─────▼─────┐  ┌──────▼──────┐
         │PosNoExistente │  │ColorInvalido│  │Posicion     │
         │Exception      │  │Exception    │  │Invalida     │
         └───────────────┘  └─────────────┘  └─────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                           CLASES CORE                                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Checker       │     │     Player      │     │      Dice       │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ - __color__     │     │ - __color__     │     │ - __values__    │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ + obtener_color()│    │ + obtener_color()│    │ + tirar()       │
│ + __str__()     │     │ + obtener_simbolo()   │ + obtener_valores()
└─────────────────┘     └─────────────────┘     └─────────────────┘
        ▲                       │
        │                       │ usa para símbolo
        │                       └─────────────┐
        │                                     │
        │                                     ▼
        │                            ┌─────────────────┐
        │                            │                 │
        │ contiene *                 │                 │
        │                            │                 │
┌───────┴──────────────────────┐    │                 │
│        Board                  │    │                 │
├───────────────────────────────┤    │                 │
│ - __points__: list[list]      │    │      Game       │
│ - __bar__: dict               │    │                 │
│ - __off__: dict               │    ├─────────────────┤
├───────────────────────────────┤    │ - tablero       │◆─────┐
│ + setup()                     │    │ - dados         │      │
│ + get_point(pos)              │    │ - jugadores     │      │
│ + mover(ori, dest, col)       │◆───┤ - turno_actual  │      │
│ + capturar(pos, col)          │    ├─────────────────┤      │
│ + sacar(pos, col)             │    │ + mover()       │      │
│ + puede_mover(...)            │    │ + gano()        │      │
│ + puede_sacar_ficha()         │    │ + hay_movimientos()   │
│ + mostrar()                   │    │ + puede_sacar_ficha() │
└───────────────────────────────┘    │ + cambiar_turno()│     │
                                     └─────────┬────────┘     │
                                               │              │
                                        contiene 2            │
                                               │              │
                                     ┌─────────▼────────┐     │
                                     │     Player       │     │
                                     └──────────────────┘     │
                                                             │
                                              ┌──────────────▼──┐
                                              │      Dice       │
                                              └─────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         INTERFACES DE USUARIO                                │
└─────────────────────────────────────────────────────────────────────────────┘

        ┌─────────────────┐              ┌─────────────────┐
        │      CLI        │              │   PygameUI      │
        ├─────────────────┤              ├─────────────────┤
        │ - juego: Game   │              │ - juego: Game   │
        ├─────────────────┤              ├─────────────────┤
        │ + jugar()       │              │ + run()         │
        │ + mostrar_estado()            │ + draw_board()  │
        └────────┬────────┘              └────────┬────────┘
                 │                                │
                 │ usa                            │ usa
                 │                                │
                 └───────────┐        ┌───────────┘
                             │        │
                             ▼        ▼
                         ┌────────────────┐
                         │     Game       │
                         └────────────────┘




### 8.2. Flujo de Ejecución Típico

```
1. main.py inicia
   ↓
2. Usuario elige CLI o Pygame
   ↓
3. Se crea Game con Board, Dice, Players
   ↓
4. CLI/Pygame entra en loop principal:
   a. Mostrar estado (tablero, dados, turno)
   b. Tirar dados
   c. Solicitar movimientos al usuario
   d. Ejecutar movimientos (Game.mover)
   e. Verificar victoria (Game.gano)
   f. Cambiar turno si no hay más movimientos
   g. Repetir hasta que alguien gane
   ↓
5. Mostrar ganador
   ↓
6. Fin del juego
```

### 8.3. Flujo Básico de Movimiento

Cuando el usuario hace un movimiento: CLI solicita origen y pasos → Game valida con dados y estado actual → Game verifica que no hay fichas en barra → Board valida si la posición es legal → Board ejecuta el movimiento (remueve de origen, captura si hay enemigo, agrega a destino) → CLI muestra tablero actualizado.

---



**Fecha de última actualización:** 31 de Octubre, 2025  
**Autor:** [Tu Nombre]  
**Versión:** 1.0