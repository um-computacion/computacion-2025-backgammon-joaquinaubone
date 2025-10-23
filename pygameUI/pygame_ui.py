"""Interfaz gráfica del juego de Backgammon usando Pygame."""
import sys
from pathlib import Path
import pygame
import copy
# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from game.game import Juego
from board.board import Tablero
from dice.dice import Dice
from player.player import Player

# ------------------ Config visual ------------------
WIDTH, HEIGHT = 1000, 700
MARGIN_X, MARGIN_Y = 40, 40
BG_COLOR = (245, 239, 230)
BOARD_COLOR = (230, 220, 200)
TRI_A = (170, 120, 90)
TRI_B = (210, 170, 130)
LINE = (60, 60, 60)
WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
TEXT = (25, 25, 25)
HIGHLIGHT = (100, 200, 100)

MAX_VISIBLE_STACK = 5


def point_index_to_display(idx):
    """Convierte índice 0..23 a (row, columna_visual).
    
    Args:
        idx: índice del punto (0-23)
    
    Returns:
        tuple: ('top' o 'bottom', columna_visual 0-11)
    """
    if 0 <= idx <= 11:
        return 'top', 11 - idx
    return 'bottom', idx - 12


def draw_triangle_in_area(surface, area_rect, col_index, row, color, highlight=False):
    """Dibuja un triángulo dentro de un área específica.
    
    Args:
        surface: superficie de pygame
        area_rect: rectángulo del área (left_rect o right_rect)
        col_index: índice de columna dentro del área (0-5)
        row: 'top' o 'bottom'
        color: color RGB del triángulo
        highlight: si debe resaltarse
    """
    tri_w = area_rect.width / 6.0
    x0 = area_rect.left + col_index * tri_w
    x1 = x0 + tri_w
    x_mid = (x0 + x1) / 2.0

    if row == 'top':
        tip_y = area_rect.top + area_rect.height * 0.42
        pts = [(x0, area_rect.top), (x1, area_rect.top), (x_mid, tip_y)]
    else:
        tip_y = area_rect.bottom - area_rect.height * 0.42
        pts = [(x0, area_rect.bottom), (x1, area_rect.bottom), (x_mid, tip_y)]

    final_color = HIGHLIGHT if highlight else color
    pygame.draw.polygon(surface, final_color, pts)

def draw_checker(surface, center, radius, color_rgb, label=None, font=None):
    """Dibuja una ficha circular.
    
    Args:
        surface: superficie de pygame
        center: tupla (x, y) del centro
        radius: radio de la ficha
        color_rgb: color RGB de la ficha
        label: texto opcional para mostrar en la ficha
        font: fuente de pygame para el label
    """
    pygame.draw.circle(surface, color_rgb, center, radius)
    pygame.draw.circle(surface, LINE, center, radius, 1)
    if label and font:
        txt = font.render(str(label), True,
                         LINE if color_rgb == WHITE else WHITE)
        rect = txt.get_rect(center=center)
        surface.blit(txt, rect)

def render_board(surface, tablero, font, selected_point=None, destinos_validos=None):
    """Dibuja el tablero con barra separada, resalta origen y destinos válidos.
    
    Args:
        surface: superficie de Pygame
        tablero: instancia de Tablero
        font: fuente de Pygame
        selected_point: punto seleccionado para resaltar (opcional)
        destinos_validos: lista de índices de destinos válidos (opcional)
    
    Returns:
        tuple: (hitmap, board_rect)
    """
    if destinos_validos is None:
        destinos_validos = []
    
    surface.fill(BG_COLOR)

    # Marco del tablero COMPLETO
    full_board_rect = pygame.Rect(
        MARGIN_X, MARGIN_Y + 20,
        WIDTH - 2 * MARGIN_X, HEIGHT - 2 * MARGIN_Y - 40
    )
    pygame.draw.rect(surface, BOARD_COLOR, full_board_rect, border_radius=12)
    pygame.draw.rect(surface, LINE, full_board_rect, 2, border_radius=12)

    # Dividir en 3 zonas: izquierda (6 puntos), barra, derecha (6 puntos)
    bar_width = 80
    usable_width = full_board_rect.width - bar_width
    left_width = usable_width // 2
    right_width = usable_width // 2

    # Rectángulos de cada zona
    left_rect = pygame.Rect(full_board_rect.left, full_board_rect.top,
                           left_width, full_board_rect.height)
    
    bar_x = full_board_rect.left + left_width
    bar_rect = pygame.Rect(bar_x, full_board_rect.top,
                          bar_width, full_board_rect.height)
    
    right_rect = pygame.Rect(bar_x + bar_width, full_board_rect.top,
                            right_width, full_board_rect.height)

    # Dibujar BARRA
    if selected_point == -1:
        pygame.draw.rect(surface, HIGHLIGHT, bar_rect)
    else:
        pygame.draw.rect(surface, (200, 180, 150), bar_rect)
    pygame.draw.rect(surface, LINE, bar_rect, 2)

    # Etiqueta "BAR"
    bar_label = font.render("BAR", True, TEXT)
    bar_label_rect = bar_label.get_rect(center=(bar_rect.centerx, full_board_rect.top - 14))
    surface.blit(bar_label, bar_label_rect)

    # Calcular ancho de cada triángulo
    tri_w_left = left_width / 6.0
    tri_w_right = right_width / 6.0
    
    radius = int(min(tri_w_left, tri_w_right) * 0.38)
    radius = max(12, min(radius, 22))
    vgap = 4
    step = radius * 2 + vgap

    # Dibujar triángulos IZQUIERDA
    for i in range(6):
        idx_top = 11 - i
        highlight_top = (selected_point == idx_top)
        draw_triangle_in_area(surface, left_rect, i, 'top',
                             TRI_A if i % 2 == 0 else TRI_B, highlight_top)
        
        idx_bottom = 12 + i
        highlight_bottom = (selected_point == idx_bottom)
        draw_triangle_in_area(surface, left_rect, i, 'bottom',
                             TRI_B if i % 2 == 0 else TRI_A, highlight_bottom)

    # Dibujar triángulos DERECHA
    for i in range(6):
        idx_top = 5 - i
        highlight_top = (selected_point == idx_top)
        draw_triangle_in_area(surface, right_rect, i, 'top',
                             TRI_A if i % 2 == 0 else TRI_B, highlight_top)
        
        idx_bottom = 18 + i
        highlight_bottom = (selected_point == idx_bottom)
        draw_triangle_in_area(surface, right_rect, i, 'bottom',
                             TRI_B if i % 2 == 0 else TRI_A, highlight_bottom)

    # Etiquetas superiores IZQUIERDA (12..7)
    for i in range(6):
        lbl = str(12 - i)
        x = int(left_rect.left + i * tri_w_left + tri_w_left / 2)
        y = full_board_rect.top - 14
        img = font.render(lbl, True, TEXT)
        rect = img.get_rect(center=(x, y))
        surface.blit(img, rect)

    # Etiquetas superiores DERECHA (6..1)
    for i in range(6):
        lbl = str(6 - i)
        x = int(right_rect.left + i * tri_w_right + tri_w_right / 2)
        y = full_board_rect.top - 14
        img = font.render(lbl, True, TEXT)
        rect = img.get_rect(center=(x, y))
        surface.blit(img, rect)

    # Etiquetas inferiores IZQUIERDA (13..18)
    for i in range(6):
        lbl = str(13 + i)
        x = int(left_rect.left + i * tri_w_left + tri_w_left / 2)
        y = full_board_rect.bottom + 14
        img = font.render(lbl, True, TEXT)
        rect = img.get_rect(center=(x, y))
        surface.blit(img, rect)

    # Etiquetas inferiores DERECHA (19..24)
    for i in range(6):
        lbl = str(19 + i)
        x = int(right_rect.left + i * tri_w_right + tri_w_right / 2)
        y = full_board_rect.bottom + 14
        img = font.render(lbl, True, TEXT)
        rect = img.get_rect(center=(x, y))
        surface.blit(img, rect)

    # Líneas horizontales centrales
    pygame.draw.line(surface, LINE,
                    (left_rect.left, left_rect.centery),
                    (left_rect.right, left_rect.centery), 1)
    pygame.draw.line(surface, LINE,
                    (right_rect.left, right_rect.centery),
                    (right_rect.right, right_rect.centery), 1)

    # --- CREAR HITMAP ---
    hitmap = {i: [] for i in range(24)}
    hitmap[-1] = []

    # Dibujar fichas en BARRA
    bar_blanco = tablero.obtener_bar('B')
    bar_negro = tablero.obtener_bar('N')
    
    if bar_blanco:
        start_y = bar_rect.bottom - radius - 6
        for i in range(min(len(bar_blanco), MAX_VISIBLE_STACK)):
            cy = start_y - i * step
            label = len(bar_blanco) if i == min(len(bar_blanco), MAX_VISIBLE_STACK) - 1 and len(bar_blanco) > MAX_VISIBLE_STACK else None
            draw_checker(surface, (bar_rect.centerx, cy), radius, WHITE, label, font)
            hitmap[-1].append((bar_rect.centerx, cy, radius))
    
    if bar_negro:
        start_y = bar_rect.top + radius + 6
        for i in range(min(len(bar_negro), MAX_VISIBLE_STACK)):
            cy = start_y + i * step
            label = len(bar_negro) if i == min(len(bar_negro), MAX_VISIBLE_STACK) - 1 and len(bar_negro) > MAX_VISIBLE_STACK else None
            draw_checker(surface, (bar_rect.centerx, cy), radius, BLACK, label, font)
            hitmap[-1].append((bar_rect.centerx, cy, radius))

    # Convertir tablero a formato Pygame
    pos = tablero.to_pygame_format()

    # Dibujar fichas en puntos
    for idx, cell in enumerate(pos):
        if not cell:
            continue
        color_name, count = cell
        
        # Determinar en qué zona está
        if 7 <= idx <= 11:
            col_vis = 11 - idx
            area_rect = left_rect
            tri_w = tri_w_left
            row = 'top'
        elif 12 <= idx <= 17:
            col_vis = idx - 12
            area_rect = left_rect
            tri_w = tri_w_left
            row = 'bottom'
        elif 0 <= idx <= 5:
            col_vis = 5 - idx
            area_rect = right_rect
            tri_w = tri_w_right
            row = 'top'
        else:
            col_vis = idx - 18
            area_rect = right_rect
            tri_w = tri_w_right
            row = 'bottom'
        
        cx = int(area_rect.left + col_vis * tri_w + tri_w / 2)

        if row == 'top':
            start_y = int(area_rect.top + radius + 6)
            visibles = min(count, MAX_VISIBLE_STACK)
            extras = max(0, count - (MAX_VISIBLE_STACK - 1)) \
                     if count > MAX_VISIBLE_STACK else 0
            for i in range(visibles):
                cy = start_y + i * step
                label = extras if (extras and i == visibles - 1) else None
                draw_checker(surface, (cx, cy), radius,
                           WHITE if color_name == 'white' else BLACK,
                           label, font)
                hitmap[idx].append((cx, cy, radius))
        else:
            start_y = int(area_rect.bottom - radius - 6)
            visibles = min(count, MAX_VISIBLE_STACK)
            extras = max(0, count - (MAX_VISIBLE_STACK - 1)) \
                     if count > MAX_VISIBLE_STACK else 0
            for i in range(visibles):
                cy = start_y - i * step
                label = extras if (extras and i == visibles - 1) else None
                draw_checker(surface, (cx, cy), radius,
                           WHITE if color_name == 'white' else BLACK,
                           label, font)
                hitmap[idx].append((cx, cy, radius))

    # --- DIBUJAR CÍRCULOS VERDES Y AGREGAR AL HITMAP (AL FINAL) ---
    if destinos_validos:
        for dest_idx in destinos_validos:
            # Determinar posición
            if 7 <= dest_idx <= 11:
                col_vis = 11 - dest_idx
                area_rect = left_rect
                tri_w = tri_w_left
            elif 12 <= dest_idx <= 17:
                col_vis = dest_idx - 12
                area_rect = left_rect
                tri_w = tri_w_left
            elif 0 <= dest_idx <= 5:
                col_vis = 5 - dest_idx
                area_rect = right_rect
                tri_w = tri_w_right
            else:
                col_vis = dest_idx - 18
                area_rect = right_rect
                tri_w = tri_w_right
            
            cx = int(area_rect.left + col_vis * tri_w + tri_w / 2)
            cy = area_rect.centery
            
            # Dibujar círculo verde
            pygame.draw.circle(surface, HIGHLIGHT, (cx, cy), 25, 4)
            
            # AGREGAR al hitmap para que sea clickeable
            hitmap[dest_idx].append((cx, cy, 30))

    return hitmap, full_board_rect

def hit_test(hitmap, pos):
    """Detecta si se clickeó una ficha.
    
    Args:
        hitmap: diccionario con círculos por punto
        pos: posición del mouse (x, y)
    
    Returns:
        int o None: índice del punto (0..23) o None
    """
    mx, my = pos
    for idx, circles in hitmap.items():
        for (cx, cy, r) in circles:
            dx, dy = mx - cx, my - cy
            if dx*dx + dy*dy <= r*r:
                return idx
    return None


def draw_dice(surface, dice_values, font):
    """Dibuja los dados en la parte superior.
    
    Args:
        surface: superficie de pygame
        dice_values: lista con valores de los dados
        font: fuente de pygame
    """
    x_start = 50
    y = 20
    for val in dice_values:
        txt = font.render(f"🎲 {val}", True, TEXT)
        surface.blit(txt, (x_start, y))
        x_start += 80


def draw_message(surface, message, font, color=TEXT):
    """Dibuja mensaje en la parte inferior.
    
    Args:
        surface: superficie de pygame
        message: texto del mensaje
        font: fuente de pygame
        color: color del texto
    """
    txt = font.render(message, True, color)
    rect = txt.get_rect(center=(WIDTH // 2, HEIGHT - 30))
    surface.blit(txt, rect)

def calcular_destinos_validos(juego, origen, dados_disponibles, color):
    """Calcula destinos válidos desde un origen con los dados disponibles.
    
    NO modifica el tablero, solo calcula teóricamente los destinos.
    
    Returns:
        list: Lista de índices de destino válidos
    """
    destinos = []
    
    for dado in dados_disponibles:
        # Calcular destino teórico
        if origen == -1:
            # Desde la barra
            if color == 'B':
                destino = dado - 1  # Blancas entran por 1-6 (índices 0-5)
            else:
                destino = 24 - dado  # Negras entran por 24-19 (índices 23-18)
        else:
            # Movimiento normal
            if color == 'B':
                destino = origen + dado
            else:
                destino = origen - dado
        
        # Verificar que el destino esté dentro del tablero
        if 0 <= destino <= 23:
            # Ahora SÍ verificar si es válido haciendo una copia temporal
            tablero_temp = copy.deepcopy(juego.tablero)
            juego_temp = copy.deepcopy(juego)
            
            try:
                juego_temp.mover(origen, dado)
                # Si no lanzó excepción, el movimiento es válido
                if destino not in destinos:
                    destinos.append(destino)
            except (ValueError, Exception):
                # Movimiento inválido, no agregar
                pass
    
    return destinos

def main():
    """Función principal de la interfaz Pygame."""
    print("=== INICIANDO PYGAME ===")
    
    try:
        pygame.init()
        print("✓ Pygame inicializado")
        
        pygame.display.set_caption("Backgammon (Pygame)")
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        print("✓ Ventana creada")
        
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 20)
        print("✓ Fuente cargada")

        # Crear tablero y configurar posición inicial
        print("Creando tablero...")
        tablero = Tablero()
        print("✓ Tablero creado")
        
        tablero.setup()
        print("✓ Tablero configurado")

        hitmap = {}

        print("=== ENTRANDO AL LOOP ===")
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    print("Cerrando por QUIT")
                    running = False
                elif e.type == pygame.KEYDOWN and e.key in (pygame.K_ESCAPE,
                                                             pygame.K_q):
                    print("Cerrando por ESC/Q")
                    running = False
                elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    idx = hit_test(hitmap, e.pos)
                    if idx is not None:
                        print(f"Clickeaste el punto {idx}")

            # Renderizar
            hitmap = render_board(screen, tablero, font)

            pygame.display.flip()
            clock.tick(60)

        print("=== CERRANDO PYGAME ===")
        pygame.quit()
        sys.exit()
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
if __name__ == '__main__':
    main()