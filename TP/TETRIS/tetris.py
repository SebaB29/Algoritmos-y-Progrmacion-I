from random import choice

ANCHO_JUEGO, ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1
PIEZA_ACTUAL = "@"
POSICION_LIBRE = ""
POSICION_OCUPADA = "#"

CUBO = 0
Z = 1
S = 2
I = 3
L = 4
L_INV = 5
T = 6

PIEZAS = (
    ((0, 0), (1, 0), (0, 1), (1, 1)), # Cubo
    ((0, 0), (1, 0), (1, 1), (2, 1)), # Z (zig-zag)
    ((0, 0), (0, 1), (1, 1), (1, 2)), # S (-Z)
    ((0, 0), (0, 1), (0, 2), (0, 3)), # I (línea)
    ((0, 0), (0, 1), (0, 2), (1, 2)), # L
    ((0, 0), (1, 0), (2, 0), (2, 1)), # -L
    ((0, 0), (1, 0), (2, 0), (1, 1)), # T
)

def generar_pieza(pieza=None):
    """
    Genera una nueva pieza de entre PIEZAS al azar. Si se especifica el parámetro pieza
    se generará una pieza del tipo indicado. Los tipos de pieza posibles
    están dados por las constantes CUBO, Z, S, I, L, L_INV, T.

    El valor retornado es una tupla donde cada elemento es una posición
    ocupada por la pieza, ubicada en (0, 0). Por ejemplo, para la pieza
    I se devolverá: ( (0, 0), (0, 1), (0, 2), (0, 3) ), indicando que 
    ocupa las posiciones (x = 0, y = 0), (x = 0, y = 1), ..., etc.
    """

    if not pieza:
        pieza = choice([CUBO, Z, S, I, L, L_INV, T])

    return PIEZAS[pieza]

def trasladar_pieza(pieza, dx, dy):
    """
    Traslada la pieza de su posición actual a (posicion + (dx, dy)).

    La pieza está representada como una tupla de posiciones ocupadas,
    donde cada posición ocupada es una tupla (x, y). 
    Por ejemplo para la pieza ( (0, 0), (0, 1), (0, 2), (0, 3) ) y
    el desplazamiento dx=2, dy=3 se devolverá la pieza 
    ( (2, 3), (2, 4), (2, 5), (2, 6) ).
    """

    return tuple((coordenada_x + dx, coordenada_y + dy) for coordenada_x, coordenada_y in pieza)

def crear_juego(pieza_inicial):
    """
    Crea un nuevo juego de Tetris.

    El parámetro pieza_inicial es una pieza obtenida mediante 
    pieza.generar_pieza. Ver documentación de esa función para más información.

    El juego creado debe cumplir con lo siguiente:
    - La grilla está vacía: hay_superficie da False para todas las ubicaciones
    - La pieza actual está arriba de todo, en el centro de la pantalla.
    - El juego no está terminado: terminado(juego) da False

    Que la pieza actual esté arriba de todo significa que la coordenada Y de 
    sus posiciones superiores es 0 (cero).
    """

    juego = [[POSICION_LIBRE for columna in range(ANCHO_JUEGO)] for fila in range(ALTO_JUEGO)]
    colocar_pieza(juego, trasladar_pieza(pieza_inicial, ANCHO_JUEGO // 2, 0))

    return juego

def dimensiones(juego):
    """
    Devuelve las dimensiones de la grilla del juego como una tupla (ancho, alto).
    """

    return (len(juego[0]), len(juego))

def pieza_actual(juego):
    """
    Devuelve una tupla de tuplas (x, y) con todas las posiciones de la
    grilla ocupadas por la pieza actual.

    Se entiende por pieza actual a la pieza que está cayendo y todavía no
    fue consolidada con la superficie.

    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """

    return tuple((columna, fila) for fila in range(len(juego)) \
                                 for columna in range(len(juego[fila])) \
                                 if juego[fila][columna] == PIEZA_ACTUAL)

def hay_superficie(juego, x, y):
    """
    Devuelve True si la celda (x, y) está ocupada por la superficie consolidada.
    
    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """

    return juego[y][x] == POSICION_OCUPADA

def mover(juego, direccion):
    """
    Mueve la pieza actual hacia la derecha o izquierda, si es posible.
    Devuelve un nuevo estado de juego con la pieza movida o el mismo estado 
    recibido si el movimiento no se puede realizar.

    El parámetro direccion debe ser una de las constantes DERECHA o IZQUIERDA.
    """

    posicion_pieza_actual = trasladar_pieza(pieza_actual(juego), direccion, 0)

    if esta_en_posicion_valida(juego, posicion_pieza_actual):
        for coordenada_x, coordenada_y in posicion_pieza_actual:
            juego[coordenada_y][coordenada_x - direccion] = POSICION_LIBRE

        colocar_pieza(juego, posicion_pieza_actual)

    return juego

def avanzar(juego, siguiente_pieza):
    """
    Avanza al siguiente estado de juego a partir del estado actual.
    
    Devuelve una tupla (juego_nuevo, cambiar_pieza) donde el primer valor
    es el nuevo estado del juego y el segundo valor es un booleano que indica
    si se debe cambiar la siguiente_pieza (es decir, se consolidó la pieza
    actual con la superficie).
    
    Avanzar el estado del juego significa:
     - Descender una posición la pieza actual.
     - Si al descender la pieza no colisiona con la superficie, simplemente
       devolver el nuevo juego con la pieza en la nueva ubicación.
     - En caso contrario, se debe
       - Consolidar la pieza actual con la superficie.
       - Eliminar las líneas que se hayan completado.
       - Cambiar la pieza actual por siguiente_pieza.

    Si se debe agregar una nueva pieza, se utilizará la pieza indicada en
    el parámetro siguiente_pieza. El valor del parámetro es una pieza obtenida 
    llamando a generar_pieza().

    **NOTA:** Hay una simplificación respecto del Tetris real a tener en
    consideración en esta función: la próxima pieza a agregar debe entrar 
    completamente en la grilla para poder seguir jugando, si al intentar 
    incorporar la nueva pieza arriba de todo en el medio de la grilla se
    pisara la superficie, se considerará que el juego está terminado.

    Si el juego está terminado (no se pueden agregar más piezas), la funcion no hace nada, 
    se debe devolver el mismo juego que se recibió.
    """

    posicion_pieza_actual = trasladar_pieza(pieza_actual(juego), 0, 1)
    cambiar_pieza = False

    if esta_en_posicion_valida(juego, posicion_pieza_actual):
        for coordenada_x, coordenada_y in posicion_pieza_actual:
            juego[coordenada_y - 1][coordenada_x] = POSICION_LIBRE

        colocar_pieza(juego, posicion_pieza_actual)

    else:
        consolidar_pieza(juego, posicion_pieza_actual)
        juego = eliminar_filas(juego)
        siguiente_pieza = trasladar_pieza(siguiente_pieza, ANCHO_JUEGO // 2, 0)

        if esta_en_posicion_valida(juego, siguiente_pieza):
            colocar_pieza(juego, siguiente_pieza)

        if not terminado(juego):
            cambiar_pieza = True

    return juego, cambiar_pieza

def terminado(juego):
    """
    Devuelve True si el juego terminó, es decir no se pueden agregar
    nuevas piezas, o False si se puede seguir jugando.
    """

    for fila in juego:
        if PIEZA_ACTUAL in fila:
            return False

    return True

def colocar_pieza(juego, pieza):
    """
    -Recibe: la grilla y una pieza
    -Coloca la pieza dentro de la grilla
    """

    for coordenada_x, coordenada_y in pieza:
        juego[coordenada_y][coordenada_x] = PIEZA_ACTUAL

def consolidar_pieza(juego, pieza):
    """
    -Recibe: la grilla y la posicion de la pieza actual
    -Convierte la pieza en superficie consolidada
    """

    for coordenada_x, coordenada_y in pieza:
        juego[coordenada_y - 1][coordenada_x] = POSICION_OCUPADA

def eliminar_filas(juego):
    """
    -Recibe: la grilla
    -Devuelve: una nueva grilla sin filas completas
    """

    nuevo_juego = []
    for fila in juego:
        if not POSICION_LIBRE in fila:
            nuevo_juego.insert(0, [POSICION_LIBRE for columna in range(ANCHO_JUEGO)])
        else:
            nuevo_juego.append(fila)

    return nuevo_juego

def esta_en_posicion_valida(juego, pieza):
    """
    -Recibe: la grilla y la pieza
    -Devuelve:
    - True, si la pieza esta dentro de rango y no colisiona
    - False, si la pieza colisiona con el limite inferior de la grilla o con la superficie consolidada o si esta fuera de rango
    """

    for coordenada_x, coordenada_y in pieza:
        if not (0 <= coordenada_x < ANCHO_JUEGO) or not (0 <= coordenada_y < ALTO_JUEGO) or hay_superficie(juego, coordenada_x, coordenada_y):
            return False

    return True