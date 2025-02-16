def encriptar(mensaje, n):
    ans = ""
    alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for ch in mensaje:
        if ch.islower():
            ch = ch.upper()

        if ch in alf:
            index = (alf.index(ch) + n) % 26
            ans += alf[index]
        else:
            ans += ch  

    return ans


def desencriptar(mensaje, n):
    ans = ""
    alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for ch in mensaje:
        if ch.islower():
            ch = ch.upper()

        if ch in alf:
            index = (alf.index(ch) - n) % 26
            ans += alf[index]
        else:
            ans += ch  

    return ans


mensaje = "Eres dinamita nena"
n = 5

print("El texto original es: " + mensaje)
print("El valor de cambio de posición es: " + str(n))

mensaje_cifrado = encriptar(mensaje, n)
print("El texto cifrado es: " + mensaje_cifrado)


print("El texto descifrado es: " + desencriptar(mensaje_cifrado, n))
