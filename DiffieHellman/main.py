numPrimo = 33331
numGen = 5


def validarNum(numPrimo, numGen):
    if numPrimo <= numGen or numPrimo < 2:
        return False
    for i in range(2, int(numPrimo ** 0.5) + 1):
        if numPrimo % i == 0:
            return False
    return True


def llavePublicaA(llaveA):
   
    llavePA = (numGen ** llaveA) % numPrimo
    
    return llavePA
    
    
def llavePublicaB(llaveB):
    
    llavePB = (numGen ** llaveB) % numPrimo
    
    return llavePB
    
    
def llaveCompartidaA(llavePubB, llavePrivA):
    
    llaveCompartida = (llavePubB ** llavePrivA) % numPrimo
    
    return llaveCompartida
    
    
def llaveCompartidaB(llavePubA, llavePrivB):
    
    llaveCompartida = (llavePubA ** llavePrivB) % numPrimo
    
    return llaveCompartida
    

if not validarNum(numPrimo, numGen):
    print("El numero primo no es válido.")
else:
    
    llavePrivA = 5
    llavePrivB = 3
    llavePubA = llavePublicaA(llavePrivA) 
    llavePubB = llavePublicaB(llavePrivB) 
    print("La llave Publica A es: " + str(llavePubA))
    print("La llave Publica B es: " + str(llavePubB))
    
    llaveCompA = llaveCompartidaA(llavePubB, llavePrivA) 
   
    print("La llave compartida con llave Privada B y llave Publica A es: " + str(llaveCompA))
    
    llaveCompB = llaveCompartidaB(llavePubA, llavePrivB) 
   
    print("La llave compartida con llave Privada A y llave Publica B es: " + str(llaveCompB))
    
    
    
    
    
    