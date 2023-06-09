lista=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def busqueda_binaria_recursiva(arreglo, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = arreglo[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:  
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_binaria_recursiva(arreglo, busqueda,izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_binaria_recursiva(arreglo, busqueda, indiceDelElementoDelMedio + 1, derecha)
    
print(busqueda_binaria_recursiva(lista,16,lista[0],lista[-1]))

#De acuerdo al teorema del Maestro este algoritmo tiene una complejidad de O(logn) ya que primero "a" tiene una cantidad de llamados recursivos de 1, después n/b es igual a n/2
#ya que el tamaño de la entrada siempre busca dividirse en 2, por lo tanto b=2 y finalmente tenemos que O(1) ya que las operaciones son en tiempo constante, por lo tanto c=0
#Finalmente sustituyendo tenemos que O(logn).
