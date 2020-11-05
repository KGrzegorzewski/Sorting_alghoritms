from sortowanie import *
from timeit import timeit
import random
import os
import sys

sys.setrecursionlimit(1000000)


def wczytaj_wyrazy(nazwa_pliku, tablica):
	i = 0
	plik = open(nazwa_pliku, encoding="utf8")
	for linia in plik:
		for word in linia.split():
			tablica[i] = word
			i += 1
			
	return tablica

count = 69063
input_list = [None] * count
nr_of_sorts = 1


print(wczytaj_wyrazy("pan-tadeusz.txt", input_list))


ile = 0

for word in range(len(input_list)):
	if input_list[word] != None:
		ile += 1
		
		
print(ile)


nr_of_sorts = 1


# Nie wiem czy w takim razie są potrzebne te kopiowania 
bub_arr = input_list.copy()
sel_arr = input_list.copy()
merge_arr = input_list.copy()
quick_arr = input_list.copy()



# Listy do przechowywania wartosci czasow dla n pierwszych wartosci pliku pan-tadeusz.txt

time_bubble = []
time_selection =[]
time_merge = []
time_quick =[]


n = [5000, 10000, 25000, 40000, count]
for time in n:
	time_bubble.append(round(timeit(lambda: merge_sort(input_list[:time]), number = nr_of_sorts), 3))
	time_selection.append(round(timeit(lambda: selection_sort(input_list[:time]), number = nr_of_sorts), 3))
	time_merge.append(round(timeit(lambda: merge_sort(input_list[:time]), number = nr_of_sorts), 3))
	time_quick.append(round(timeit(lambda: quickSort(input_list[:time], 0, time-1), number = nr_of_sorts), 3))
	
print("Czasy dla sortowania bubble_sort", time_bubble)
print("Czasy dla sortowania selection_sort", time_selection)
print("Czasy dla sortowania merge_sort", time_merge)
print("Czasy dla sortowania quicksort", time_quick)
	
	

#big_arr = [random.random() for _ in range(10000)]
























