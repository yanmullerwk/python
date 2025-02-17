

def ordena_lista(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr

lista = [2, 23, 5, 12, 20, 3]
print(ordena_lista(lista))