import datetime

def semana_actual():
    return datetime.date.today().isocalendar()[1]

def mes_actual():
    return datetime.datetime.now().month

def unirListas(l1,l2):
    result = []
    for i in l1:
        result.add(i)
    for i in l2:
        result.add(i)
    return result

def intersectarListas(l1,l2):
    result = []
    for i in l1:
        for j in l2:
            if i == j:
                result.append(i)
    return result

def diferenciaListas(l1,l2):
    result = l1
    for i in l2:
        if i in result:
            result.remove(i)
    return result

def setL(lista):
    set = []
    for x in lista:
        if x not in set:
            set.append(x)
    return set

def ordenar_por(mat, para):
    for i in range(0, len(mat) - 1):
        for j in range(i + 1, len(mat)):
            if (mat[i][para] > mat[j][para]):
                aux = mat[i]
                mat[i] = mat[j]
                mat[j] = aux
    return mat

def ordenar_por_inv(mat, para):
    for i in range(0, len(mat) - 1):
        for j in range(i + 1, len(mat)):
            if (mat[i][para] < mat[j][para]):
                aux = mat[i]
                mat[i] = mat[j]
                mat[j] = aux
    return mat
