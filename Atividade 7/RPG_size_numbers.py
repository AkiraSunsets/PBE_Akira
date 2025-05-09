print("RPG - small,medium,large")

def size_number(number):
    if number <= 5:
        print(f"O número {number} é pequeno!")
    
    elif number <= 10:
        print(f"O número {number} é medio!")
    
    else:
        print(f"O número {number} é grande!")

size_number(3)
size_number(9)
size_number(12)
