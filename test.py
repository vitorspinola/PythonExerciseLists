def QuickSort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[(len(arr) // 2)]

		left = []
		middle = []
		right = []

		for x in arr:
			if x < pivot:
				left.append(x)
			elif x > pivot:
				right.append(x)
			elif x == pivot: 
				middle.append(x)
	return QuickSort(left) + middle + QuickSort(right)
		

		

lista = [5,6,8,9,65,12,-23,34,67,89]
lista_ordenada = QuickSort(lista)
print(lista_ordenada)