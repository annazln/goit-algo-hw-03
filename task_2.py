import random

def get_numbers_ticket(min_val, max_val, quantity): # Перевірка коректності вхідних параметрів
    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []
    
    numbers = set() # Генерація унікальних випадкових чисел
    while len(numbers) < quantity:
        numbers.add(random.randint(min_val, max_val))
    
    return sorted(numbers)


def get_user_input(): # Отримання вводу від користувача з перевіркою на коректність значень
    try:
        min_val = int(input("Введіть мінімальне можливе число (не менше 1): "))
        max_val = int(input("Введіть максимальне можливе число (не більше 1000): "))
        quantity = int(input("Введіть кількість чисел, які потрібно вибрати: "))
        return min_val, max_val, quantity
    
    except ValueError:
        print("Помилка вводу! Будь ласка, введіть коректні числові значення.")
        return None, None, None

min_val, max_val, quantity = get_user_input()

if min_val is not None and max_val is not None and quantity is not None:
    
    result = get_numbers_ticket(min_val, max_val, quantity) # Генерація та виведення випадкових чисел
    if result:
        print("Згенерований набір чисел:", result)
    else:
        print("Параметри не відповідають заданим обмеженням. Порожній список.")
else:
    print("Невірний ввід, програма завершена.")











