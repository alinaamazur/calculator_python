def kalkulator():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")

    if operacja == "+":
        print(f"Wynik: {a + b}")
    elif operacja == "-":
        print(f"Wynik: {a - b}")
    elif operacja == "*":
        print(f"Wynik: {a * b}")
    elif operacja == "/":
        if b != 0:
            print(f"Wynik: {a / b}")
        else:
            print("Błąd: Dzielenie przez zero!")
    else:
        print("Nieznana operacja!")

kalkulator()
