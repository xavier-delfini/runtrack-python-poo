x = int(input("Veuillez entrer votre nombre"))
n = int(input("Veuillez entrer votre puissance"))

i = n
n = x


def puissance(x, n, i):
    if i != 1:
        i -= 1
        x = puissance(x * n, n, i)
        return x

    else:
        return x


print(puissance(x, n, i))