# Na imprezie instytutowej pojawiają się pracownicy danego wydziału.
# Pracownicy mają swoich podwładnych, a ci podwładni mogą mieć swoich podwładnych.
# Pracownicy mają również współczynnik zabawy.
# Napisz algorytm, który pozwoli ci odpowiedziaę na pytanie - kogo zaprosić na imprezę,
# aby miała jak największy współczynnki zabawy i aby nie pojawiły się na niej żadne pary
# pracownik - bezpośredni pracodawca


class Employee:
    def __init__(self, fun):
        self.emp = []
        self.f = -1
        self.g = -1
        self.fun = fun


def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x, y)
    return v.f


def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g

