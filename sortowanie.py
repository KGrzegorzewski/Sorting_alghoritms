def bubble_sort(lista):
  n = len(lista)
  for i in range(n):
    for j in range(n-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista


def minimum(lista):
  min_val = lista[0]
  min_index = 0
  for i in range(len(lista)):
    if lista[i] < min_val:
      min_val = lista[i]
      min_index = i

  return min_index

def selection_sort(lista):
  n = len(lista)
  for i in range(n):
    index_min = minimum(lista[i:]) + i
    lista[i], lista[index_min] = lista[index_min], lista[i]
  return lista
  
  
def merge_sort(lista):
  if len(lista) > 1:
    mid = len(lista) // 2
    L = lista[:mid]
    R = lista[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        lista[k] = L[i]
        i += 1
      else:
        lista[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      lista[k] = L[i]
      i += 1
      k +=1

    while j < len(R):
      lista[k] = R[j]
      j += 1
      k += 1
 
  return lista