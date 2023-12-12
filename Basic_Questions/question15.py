def exponent(alt, ust):
    if ust < 0:
        raise ValueError("Exponent must be a non-negative integer")
    sayi = 1
    for _ in range(ust):
        sayi *= alt

    return sayi


print(exponent(2, 5))
