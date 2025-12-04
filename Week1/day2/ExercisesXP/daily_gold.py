# ===============================================
#       Daily Challenge GOLD: Happy Birthday
#       Console Version - Windows Safe
# ===============================================

from datetime import datetime

print("* Daily Challenge GOLD: Happy Birthday")

# Demander la date de naissance
birth_str = input("Enter your birthdate (DD/MM/YYYY): ")

try:
    birth_date = datetime.strptime(birth_str, "%d/%m/%Y")
    today = datetime.today()
    
    # Calculer l'age
    age = today.year - birth_date.year
    print(age)
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    # Nombre de bougies = dernier chiffre de l'âge
    candles_count = age % 10
    print(candles_count)
    if candles_count == 0:
        candles_count = 1  # toujours au moins une bougie

    candle_line = "i" * candles_count
    print(candle_line)
    cake = f"""
       ___{candle_line}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
    """

    # Vérifier année bissextile (bonus)
    is_leap = (birth_date.year % 4 == 0 and (birth_date.year % 100 != 0 or birth_date.year % 400 == 0))
    
    if is_leap:
        print("Happy Leap Year Birthday! Two cakes for you!\n")
        print(cake)
        print(cake)
    else:
        print(cake)

except ValueError:
    print("Invalid date format! Please use DD/MM/YYYY.")
