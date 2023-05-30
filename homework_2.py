a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def recu_sum(a, b):
    if a == 0:
        return b
    else:
        return recu_sum(a - 1, b + 1)


print(recu_sum(a, b))