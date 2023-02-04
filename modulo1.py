def sumarNumeros(n):
    if n <1:
        return 0
    else:
        return n+ sumarNumeros(n-1)
