'''
Дан одномерный целочисленный массив порядка N.
Найдите сумму положительных элементов массива до первого отрицательного элемента. 
Если таких элементов нет, вернуть значение 0.

'''

def sum_positive_before_negative(arr):
    
    sum = 0
    for num in arr:
        if num >= 0:
            sum += num
        else:
            break
    return sum

# Пример использования функции
arr = [1, 4, 3, -4, 5, 6]
result = sum_positive_before_negative(arr)
print(result) # выведет 6, так как сумма положительных элементов до первого отрицательного (4) равна 6

arr = [-1, -2, -3]
result = sum_positive_before_negative(arr)
print(result) # выведет 0, так как нет положительных элементов до первого отрицательного
