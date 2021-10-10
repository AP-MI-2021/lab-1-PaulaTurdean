# TURDEAN PAULA-FLORINA
def is_prime(n):
    """
    Verifica daca un numar intreg este prim sau nu.
    :param n: Un numar intreg
    :return: Returneaza True daca numarul este prim si False in caz contrar.
    """
    copie = int(n)
    if copie < 2:
        return False
    else:
        for i in range(2, copie // 2):
            if copie % i == 0:
                return False
        return True


def test_is_prime():
    assert is_prime(23) is True
    assert is_prime(14) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False


def get_product(lst):
    pass


def get_cmmdc_v1(x, y):
    """
    Determina cel mai mare divizor comun a doua numere intregi: Metoda prin scaderi repetate.
    :param x: Primul numar intreg.
    :param y: Al doilea numar intreg.
    :return: Returneaza un intreg, c.m.m.d.c - ul celor doua numere.
    """
    copiex = int(x)
    copiey = int(y)
    while copiex != copiey:
        if copiex > copiey:
            copiex = copiex - copiey
        else:
            copiey = copiey - copiex
    return copiex


def test_get_cmmdc_v1():
    assert get_cmmdc_v1(12, 18) == 6
    assert get_cmmdc_v1(3, 9) == 3


def get_cmmdc_v2(x, y):
    """
    Determina cel mai mare divizor comun a doua numere intregi: Metoda cu rest.
    :param x: Primul numar intreg.
    :param y: Al doilea numar intreg.
    :return: Returneaza un intreg, c.m.m.d.c - ul celor doua numere.
    """
    copiex = int(x)
    copiey = int(y)
    while copiey != 0:
        rest = copiex % copiey
        copiex = copiey
        copiey = rest
    return copiex


def test_get_cmmdc_v2():
    assert get_cmmdc_v1(12, 18) == 6
    assert get_cmmdc_v1(3, 9) == 3


def main():
    test_is_prime()
    test_get_cmmdc_v1()
    test_get_cmmdc_v2()
    while True:
        print("1. Determinati daca un numar este prim sau nu.")
        print("2. Determinati c.m.m.d.c - ul a doua numere prin scaderi.")
        print("3. Determinati c.m.m.d.c - ul a doua numere prin impartiri.")
        print("x. Iesire")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            numar = int(input("Dati numarul ce trebuie verificat: "))
            if is_prime(numar):
                print("DA")
            else:
                print("NU")
        elif optiune == "2":
            nr1 = int(input("Dati primul numar: "))
            nr2 = int(input("Dati al doilea numar: "))
            print("C.M.M.D.C - UL numerelor date (prin scaderi) este ", get_cmmdc_v1(nr1, nr2))
        elif optiune == "3":
            nr1 = int(input("Dati primul numar: "))
            nr2 = int(input("Dati al doilea numar: "))
            print("C.M.M.D.C - UL numerelor date (cu rest) este ", get_cmmdc_v2(nr1, nr2))
        elif optiune == "x":
            print("Ati iesit din program")
            break
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == '__main__':
    main()
