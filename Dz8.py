bruce_willis = 42
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
except ValueError:
    print("невозможно преобразовать к числу")
except IndexError:
    print("выход за границы списка")
except Exception as exc:
    print("Неожиданная ошибка типа:", type(exc))
else:
    result = bruce_willis * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
finally:
    print("Не сложнее, чем такси водить)))")
