def encriptar(mensaje, clave):
    key_arr = []
    ans = ""
    inc = 0
    alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  
    
    for y in clave:
    
        if y.islower():
            y = y.upper()
        key_arr.append(alf.index(y))
        
    for x in mensaje:
        if x.islower():
            x = x.upper()
        
        if x in alf:   
            index = (alf.index(x) + key_arr[inc % len(clave)]) % 26
            inc += 1         
            ans += alf[index]  
        else:
            ans += x 
        
    return ans
 
    
def desencriptar(mensaje, clave):
    key_arr = []
    ans = ""
    inc = 0
    alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  
    
    for y in clave:
    
        if y.islower():
            y = y.upper()
        key_arr.append(alf.index(y))
        
    for x in mensaje:
        if x.islower():
            x = x.upper()
        
        if x in alf:   
            index = (alf.index(x) - key_arr[inc % len(clave)]) % 26
            inc += 1         
            ans += alf[index]  
        else:
            ans += x 
        
    return ans


mensaje = "esto es una prueba"
clave = "Oscar"
print("El texto original es: " + mensaje)
print("La clave es: " + clave)
mensaje_cifrado = encriptar(mensaje, clave)
print("El texto cifrado es: " + mensaje_cifrado)

print("El texto descifrado es: " + desencriptar(mensaje_cifrado, clave))