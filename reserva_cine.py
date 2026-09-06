def main():
    #Creación de la matriz de asientos
    f = 3
    c = 4
    asientos = [[0 for j in range(c)] for i in range(f)]
    
    # Solicitar al usuario que ingrese la fila y columna del asiento a reservar
    print("Ingrese fila (1 a 3):")
    fila = int(input())
    print("Ingrese columna (1 a 4):")
    columna = int(input())
    asientos[fila - 1][columna - 1] = 1 

    #Imprimir el estado de la sala después de la reserva
    print("Estado de la sala:")
    for i in range(f):
        for j in range(c):
            print(asientos[i][j], end=" ")
        print()
        
main()
    