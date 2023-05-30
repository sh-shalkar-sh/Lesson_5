a = int(input("Введите число A "))
b = int(input("Введите степень числа B (целое неотрицательно число)"))


def recu(a, b):
    if b == 0:
        return 1

    return a * recu(a, b - 1)


print(recu(a, b))