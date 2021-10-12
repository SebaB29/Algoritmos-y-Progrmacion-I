import gamelib

ANCHO_VENTANA, ALTO_VENTANA = (300, 300)
MARGEN_X, MARGEN_Y = (10, 40)
ANCHO_TABLERO, ALTO_TABLERO = ((ANCHO_VENTANA - MARGEN_X * 2), (ALTO_VENTANA - MARGEN_Y * 2))
FILAS_TABLERO, COLUMNAS_TABLERO = (10, 10)
ANCHO_CELDA, ALTO_CELDA = (ANCHO_TABLERO / COLUMNAS_TABLERO, ALTO_TABLERO / FILAS_TABLERO)
JUGADOR1 = "O"
JUGADOR2 = "X"

def juego_crear():
    """Inicializar el estado del juego"""

    juego = []
    for fila in range(FILAS_TABLERO):
        juego.append([])
        for columna in range(COLUMNAS_TABLERO):
            juego[fila].append("")

    return juego

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """

    turno = decidir_turno(juego)
    if convertir_pixels_a_coordenadas(x, y):
        pos_celda_x, pos_celda_y = convertir_pixels_a_coordenadas(x, y)
        colocar_pieza_en_grilla(juego, pos_celda_x, pos_celda_y, turno)

    return juego

def convertir_pixels_a_coordenadas(pos_pixels_x, pos_pixels_y):
    """
    -Recibe: coordenadas x e y (en pixels)
    -Devuelve: las coordenadas en la grilla
    """

    if (MARGEN_X <= pos_pixels_x <= ANCHO_VENTANA - MARGEN_X) and (MARGEN_Y <= pos_pixels_y <= ALTO_VENTANA - MARGEN_Y):
        return (pos_pixels_x - MARGEN_X) // ANCHO_CELDA, (pos_pixels_y - MARGEN_Y) // ALTO_CELDA

def convertir_coordenadas_a_pixels(juego):
    """
    -Recibe: la grilla del juego
    -Devuelve: dos listas, una con las posiciones de la pieza del JUGADOR1 
    y otra con las posiciones de las piezas del JUGADOR2
    """

    pos_O = []
    pos_X = []

    for pos_celda_y, fila in enumerate(juego):
        pos_pixels_y = MARGEN_Y + pos_celda_y * ALTO_CELDA
        for pos_celda_x, columna in enumerate(fila):
            pos_pixels_x = MARGEN_X + pos_celda_x * ANCHO_CELDA

            if columna == JUGADOR1:
                pos_O.append((pos_pixels_y, pos_pixels_x))
            elif columna == JUGADOR2:
                pos_X.append((pos_pixels_y, pos_pixels_x))
    
    return pos_O, pos_X

def colocar_pieza_en_grilla(juego, pos_celda_x, pos_celda_y, turno):
    """
    -Recibe: la grilla, coordenadas x e y de la grilla, el turno
    -Coloca la pieza dentro de la grilla en las coordenadas recibidas
    """

    pos_celda_x, pos_celda_y = int(pos_celda_x), int(pos_celda_y)
    if juego[pos_celda_y][pos_celda_x] == "":
        juego[pos_celda_y][pos_celda_x] = turno

def decidir_turno(juego):
    """
    -Recibe: la grilla
    -Devuelve: el turno del jugador que le toca
    """

    cantidad_X = 0
    cantidad_O = 0
    for fila in juego:
        for columna in fila:
            if columna == "O":
                cantidad_O += 1
            elif columna == "X":
                cantidad_X += 1

    if cantidad_O > cantidad_X:
        turno = JUGADOR2
    else:
        turno = JUGADOR1
    
    return turno
    
def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', ANCHO_VENTANA // 2, 20)

    gamelib.draw_rectangle(MARGEN_X, MARGEN_Y, ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA - MARGEN_Y, fill="#000000", outline="#0020FF", width=2)

    # Divide las filas de la grilla
    pos_linea_horizontal =  MARGEN_Y + ALTO_CELDA
    for fila in range(FILAS_TABLERO - 1):
        gamelib.draw_line(MARGEN_X, pos_linea_horizontal, ANCHO_VENTANA - MARGEN_X, pos_linea_horizontal, fill="#0020FF", width=2)
        pos_linea_horizontal += ALTO_CELDA
    
    # Divide las columnas de la grilla
    pos_linea_vertical = MARGEN_X + ANCHO_CELDA
    for columna in range(COLUMNAS_TABLERO - 1):
        gamelib.draw_line(pos_linea_vertical, MARGEN_Y, pos_linea_vertical, ALTO_VENTANA - MARGEN_Y, fill="#0020FF", width=2)
        pos_linea_vertical += ANCHO_CELDA
    
    pos_O, pos_X = convertir_coordenadas_a_pixels(juego)
    for pos_pixels_y,pos_pixels_x in pos_O:
        gamelib.draw_text(JUGADOR1, pos_pixels_x + ANCHO_CELDA / 2, pos_pixels_y + ALTO_CELDA / 2, fill="#FF0000")

    for pos_pixels_y,pos_pixels_x in pos_X:
        gamelib.draw_text(JUGADOR2, pos_pixels_x + ANCHO_CELDA / 2, pos_pixels_y + ALTO_CELDA / 2, fill="#00FF00")

    gamelib.draw_text("TURNO:", ANCHO_VENTANA // 2, ALTO_VENTANA - 20)
    turno = decidir_turno(juego)
    if turno == JUGADOR1:
        gamelib.draw_text(f"{turno}", ANCHO_VENTANA // 2 + 38, ALTO_VENTANA - 20, fill="#FF0000")
    else:
        gamelib.draw_text(f"{turno}", ANCHO_VENTANA // 2 + 38, ALTO_VENTANA - 20, fill="#00FF00")

def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)