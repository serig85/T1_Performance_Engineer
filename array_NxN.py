from random import randint
print('Для создания двумерного числового массива размерностью NxN заполненного случайными числами от 0 до 10')
n = int(input('Введите число N >=3: '))
while n < 3:
    print('Число меньше трёх')
    n = int(input('Введите число N >=3: '))

arr = [[randint(0, 10) for i in range(n)] for j in range(n)]
print('Массив NxN')
for parr in arr:
    print(parr)
po_diag = []
for el_pob_diag in range(n):
    po_diag.append(arr[n-el_pob_diag-1][el_pob_diag])
print('')
print(po_diag)
po_diag.sort()
print(f'Минимальный элемент = {po_diag[0]}')
