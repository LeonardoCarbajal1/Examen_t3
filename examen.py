ENERGIA = 18
MATRIZ = """
1 1 1 1 99 1 1 1 I
1 99 99 1 99 1 99 1 99
1 1 99 1 1 1 99 1 99
99 1 99 1 99 99 99 1 99
1 1 99 -1 1 1 1 3 99
-2 99 99 1 99 99 99 1 1
1 99 1 -1 1 1 1 1 99
1 99 99 99 99 2 99 1 99
F 1 3 1 1 1 99 1 1
"""

MOV = [(0,-1),(1,0),(-1,0),(0,1)]  

def cargar(texto):
    filas = texto.strip().split("\n")
    m = []
    ini = fin = None
    for r, f in enumerate(filas):
        valores = f.split()
        fila = []
        for c, v in enumerate(valores):
            if v.upper() == "I": 
                ini = (r,c)
                fila.append(0)
            elif v.upper() == "F": 
                fin = (r,c)
                fila.append(0)
            else:
                fila.append(int(v))
        m.append(fila)
    return m, ini, fin

def dfs(m, r, c, fin, energia, visit, camino):
    if (r,c) == fin:
        return camino[:], energia

    for dr, dc in MOV:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(m) and 0 <= nc < len(m[0]) and not visit[nr][nc] and m[nr][nc] != 99:
            costo = m[nr][nc]
            if (nr,nc) == fin: costo = 0
            ne = energia - costo
            if ne >= 0:
                visit[nr][nc] = True
                camino.append((nr,nc))
                resultado = dfs(m, nr, nc, fin, ne, visit, camino)
                if resultado is not None:
                    return resultado
                camino.pop()
                visit[nr][nc] = False
    return None

def imprimir(m):
    for fila in m:
        print(" ".join(str(x) for x in fila))

def imprimir_camino(m, camino):
    temp = [[str(x) for x in fila] for fila in m]
    for r,c in camino:
        temp[r][c] = "*"
    for fila in temp:
        print(" ".join(fila))

def buscar_camino():
    m, ini, fin = cargar(MATRIZ)
    print("Laberinto:")
    imprimir(m)
    visit = [[False]*len(m[0]) for _ in m]
    visit[ini[0]][ini[1]] = True
    resultado = dfs(m, ini[0], ini[1], fin, ENERGIA, visit, [ini])
    if resultado is None:
        print("No se encontró ningún camino")
    else:
        camino, energia_restante = resultado
        print("Se encontró un camino")
        print("Energía restante:", energia_restante)
        imprimir_camino(m, camino)

buscar_camino()
