from datetime import datetime

def get_days_from_today():
    try:
        date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ") # Отримання дати
        
        date_object = datetime.strptime(date_input, '%Y-%m-%d').date() # Перетворення отриманого рядку в об'єкт
        
        today = datetime.now().date() # Поточна дата
       
        delta = today - date_object # Різниця між датами

        return delta.days
    
    except ValueError:
        return "Неправильний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'."

result = get_days_from_today()
print(result)
