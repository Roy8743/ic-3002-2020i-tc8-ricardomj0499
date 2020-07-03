A = [[0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0]]
B = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
T =[[0, 0],
     [0, 0]]
Y  = [[0], [0]]
def contar_rutas_mas_cortas(C):
    N, M = len(C), len(C[0])
    camino = []
    cont = 0
    if(N == 0 or C[N-1][M-1] == 1 or C[0][0] == 1):
        print("cont:", cont)
        return 0
    else:
        camino.append([0,0])
        return contar_rutas_mas_cortas_aux(C, 0, 0, N, M, cont, camino)

def contar_rutas_mas_cortas_aux(C, i, j, N, M, cont, caminos):
    print("i", i, "j", j)
    print("-a")
    print("caminos")
    print(caminos)
    #print("caminos", caminos)
    if(i==N-1 and j==M-1):
        print("a")
        print("cont+1")
        cont +=1
        if(len(caminos)== 0 or caminos[-1] == [0, 0]):
            print("a1")
            print("este es el ultimo CX111",cont)
            return cont
        else:
            print("a2")
            i = caminos[-1][0]
            j = caminos[-1][1]
            last = []
            while(i+1 == N or C[i+1][j] == 1 or [i+1, j] == last[0]):#len(caminos)> 0 or 
                print("t")
                print("caminos")
                print(caminos)
                
                last = []
                last.append(caminos[-1])
                print(last)
                caminos.pop(-1)
                if(len(caminos)== 0):
                    print("cont:", cont)
                    return cont
                i = caminos[-1][0]
                j = caminos[-1][1]
            temp = []
            temp.append(i+1)
            temp.append(j)
            caminos.append(temp)
            temp = []
            return contar_rutas_mas_cortas_aux(C, i+1, j, N, M, cont, caminos)
    else:
        print("a4")
        if(j+1<M and C[i][j+1] ==0):#and esta_giros(giros, i, j+1)==False 
            print("a5")
            while( j+1 < M and C[i][j+1] == 0 ):
                print("a6")
                temp = []
                temp.append(i)
                temp.append(j+1)
                caminos.append(temp)
                temp = []
                j+=1
            if(i+1  == N):
                print("a7")
                
                return contar_rutas_mas_cortas_aux(C, i, j, N, M, cont, caminos)
            else:
                print("a8")
                i+=1
                temp = []
                temp.append(i)
                temp.append(j)
                caminos.append(temp)
                temp = []
                return contar_rutas_mas_cortas_aux(C, i, j, N, M, cont, caminos)
        else:
            print("a9")
            if(i+1 < N and C[i+1][j] == 0):
                print("a10")
                i+=1
                caminos.append([i,j])
                return contar_rutas_mas_cortas_aux(C, i, j, N, M, cont, caminos)
            else:
                print("a22")
                i = caminos[-1][0]
                j = caminos[-1][1]
                last = []
                while(i+1 == N or C[i+1][j] == 1 or [i+1, j] == last[0]):
                    print()
                    print("ppppp")
                    last = []
                    last.append(caminos[-1])
                    caminos.pop(-1)
                    if(len(caminos)== 0):
                        print("ppppp1")
                        print("cont:", cont)
                        
                        return cont
                    i = caminos[-1][0]
                    j = caminos[-1][1]
                    
                print("fff")
                temp = []
                temp.append(i+1)
                temp.append(j)
                caminos.append(temp)
                temp = []
                return contar_rutas_mas_cortas_aux(C, i+1, j, N, M, cont, caminos)



contar_rutas_mas_cortas(A)

