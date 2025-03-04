def encriptar(mensaje):
    ans = ""
    alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alf_remp = ['00000010', '00000101', '00011010', '00000111', '00010110', '001001001', '00010001', '00100010', 
           '01001011', '01011001', '00000111', '00111011', '01011011', '00010101', '00001000', '00110001', 
           '00111001', '01000010', '00010000', '00110100', '00101110', '00010010', '00001100', '00100001', '00101010', '00000100']
           
    for ch in mensaje:
        if ch.islower():
            ch = ch.upper()

        if ch in alf:
            index = alf.index(ch)
            ans += alf_remp[index]
       
    return ans


def desencriptar(mensaje):
    ans = ""
    rang = ""
    alf_remp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alf = ['00000010', '00000101', '00011010', '00000111', '00010110', '001001001', '00010001', '00100010', 
           '01001011', '01011001', '00000111', '00111011', '01011011', '00010101', '00001000', '00110001', 
           '00111001', '01000010', '00010000', '00110100', '00101110', '00010010', '00001100', '00100001', '00101010', '00000100']
           
    for ch in mensaje:
        rang += ch 
        if rang in alf:
            index = alf.index(rang)          
            ans += alf_remp[index]
            rang = ""
       

    return ans
    
mensaje = "BAILA SIN CESAR"

encriptado = encriptar(mensaje)
print("El texto original es: " + mensaje)
print("El mensaje encriptado es: " + encriptado)
des = desencriptar(encriptado)
print("El mensaje desencriptado es: " + des)