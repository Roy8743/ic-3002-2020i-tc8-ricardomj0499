def contar_rutas_mas_cortas(C):
    N, M = len(C), len(C[0])
    if(N == 0 or C[N-1][M-1] == 1 or C[0][0] == 1):
        return 0
    else:
        return contar_rutas_mas_cortas_aux(C, 0, 0, N, M)

def contar_rutas_mas_cortas_aux(C, i, j, N, M):
    cont = 0
    if(i==N-1 and j==M-1):
        return 1
    elif(i==N or j==M or C[i][j] == 1):
        return 0
    else:
        cont += contar_rutas_mas_cortas_aux(C, i, j+1, N, M)
        cont += contar_rutas_mas_cortas_aux(C, i+1, j, N, M)
    return cont


