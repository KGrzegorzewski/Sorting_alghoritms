from sortowanie import *
from timeit import timeit
import random

count = 200
input_list = [None] * count
nr_of_sorts = 1

lista = [5,4,3,2,1]

big_arr = [random.random() for _ in range(10000)]
bub_arr = big_arr.copy()
sel_arr = big_arr.copy()
merge_arr = big_arr.copy()


print("Sortowanie algorytmem bubblesort trwalo: {:.3f} sekund".format(timeit(lambda: bubble_sort(bub_arr), number = nr_of_sorts)))
print("Sortowanie algorytmem selection trwalo: {:.3f} sekund".format(timeit(lambda: selection_sort(sel_arr), number = nr_of_sorts)))
print("Sortowanie algorytmem mergesort trwalo: {:.3f} sekund".format(timeit(lambda: merge_sort(merge_arr), number = nr_of_sorts)))
#print("Sortowanie quicksort babelkowym trwalo: ", timeit(lambda: bubble_sort(lista), number = 1), " sekund")