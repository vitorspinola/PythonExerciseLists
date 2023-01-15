'''Estrutura de repetição'''

def Q12_r():
	num = 1000
	counter = 1
	while num > 10 or num < 1:
		num = int(input("Insira o número que gostaria de ver a tabuada de 0 - 10: "))
	else:
		print("-----------------------------------------")
		while counter <= 10:
			mult = num * counter
			print(f"{num} x {counter} = {mult}")
			counter = counter + 1
		print("-----------------------------------------")



def Q29_r():
	#a cada produto aumenta 1 real e 98 centavos.
	counter = 1
	print("Loja Quase Dois - Tabela de Preços")
	while counter <= 50:
		based_multiplier = 1.99
		value = based_multiplier * counter
		print(f"{counter} - R$ {value:.2f}")
		counter = counter + 1
	
def Q32_r():
	import math
	user_input = int(input("Insira um número para obter o seu fatorial: "))
	counter = user_input
	subtraction_factor = 1
	print("Fatorial de", user_input)
	lista = []
	
	counter = user_input
	while counter > 0:
		lista.append(counter)
		counter = counter - 1
	total = 0
	total_total = []

		
	return print(str(lista).replace("[", "").replace("]","").replace(","," x"),"="+f" {math.prod(lista)}")
	

def Q42_r():
	print("Insira os números para verificar quais estão nos intervalos determinados pela questão. Para interromper o processo, pressione \"q\" em seu teclado.")
	nums_25 = []
	nums_50 = []
	nums_75 = []
	nums_100 = []
	while True:
		num = int(input("Número: "))
		if num < 0:
			print("+++++++++++++++++++++++++")
			break
			
		elif num >= 0 and num <= 25:
			nums_25.append(num)
			print(f"Número {num} cadastrado no processo com sucesso!")
		elif num > 25 and num <= 50:
			nums_50.append(num)
			print(f"Número {num} cadastrado no processo com sucesso!")
		elif num > 50 and num <= 75:
			nums_75.append(num)
			print(f"Número {num} cadastrado no processo com sucesso!")
		elif num > 75 and num <= 100:
			nums_100.append(num)
			print(f"Número {num} cadastrado no processo com sucesso!")
		else:
			print("Número cadastrado porém fora do escopo...")
		
		
					
	print(f"Numbers in [0-25] = {set(nums_25)}\nNumbers in [26-50] = {set(nums_50)}\nNumbers in [51-75] = {set(nums_75)}\nNumbers in [76-100] = {set(nums_100)}\n")
	
		
'''EXERCÍCIOS COM LISTAS'''

def Q01_l():
	counter = 0
	lista = []
	while counter <= 4:
		number = int(input(f"Insira o {counter+1} número: "))
		lista.append(number)
		counter += 1
	print(f"Lista de números: {lista}")


'''MAKING A QUICKSORT ALGORITHM AND LETTING CHAT GPT MAKE THE SAME ALGORITHM TO COMPARE'''
def QuickSorts(arr):
	
	
	
	def quicksortCHAT_GPT(arr):
		if len(arr) <= 1:
			return arr
		pivot = arr[len(arr) // 2]
		left = [x for x in arr if x < pivot]
		middle = [x for x in arr if x == pivot]
		right = [x for x in arr if x > pivot]
		return quicksortCHAT_GPT(left) + middle + quicksortCHAT_GPT(right)

	
	def QuickSortVitor(arr):
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
		return QuickSortVitor(left) + middle + QuickSortVitor(right)
	return QuickSortVitor and quicksortCHAT_GPT	

def heapsort(arr):
	n = len(arr)

	# Build a max heap
	for i in range(n, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)
	return arr

def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	# Compare with left child
	if l < n and arr[i] < arr[l]:
		largest = l

	# Compare with right child
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the affected sub-tree
		heapify(arr, n, largest)