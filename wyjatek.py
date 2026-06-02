try:
    a = 10
    b = "3"

    wynik = a / b
    print(wynik)
except TypeError:
    print("Nieporawna liczba!")
except ZeroDivisionError:
    print("Nie można dzielić przez 0!")
else:
    print("Działam tylko jeśli nie było błędu")
finally:
    print("wykonam się zawsze!!!")

print("To jest nowy kod od Tomka 2026")