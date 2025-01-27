from random import randint
print('Для создания двумерного числового массива размерностью NxN заполненного случайными числами от 0 до 10')
n = int(input('Введите число N: '))
arr = [[randint(0, 10) for i in range(n)] for j in range(n)]
print('Массив NxN')
for parr in arr:
    print(parr)
pob_diag = []
for el_pob_diag in range(n):
    pob_diag.append(arr[n-el_pob_diag-1][el_pob_diag])
print('')
print(pob_diag)
pob_diag.sort()
print(f'Минимальный элемент = {pob_diag[0]}')