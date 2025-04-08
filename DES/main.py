#/!/usr/bin/python3

init_permuta = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1, 
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

init_per_inv = [40, 8 ,48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9,  49, 17, 57, 25]


permu_cambio_1 = [57, 49, 41, 33, 25, 17, 9,
                   1,  58, 50, 42, 34, 26, 18,
                   10,  2, 59, 51, 43, 35, 27,
                  19, 11,  3, 60, 52, 44, 36,
                  63, 55, 47, 39, 31, 23, 15,
                   7, 62, 54, 46, 38, 30, 22,                             
                   14,  6, 61, 53, 45, 37, 29,
                  21, 13,  5, 28, 20, 12,  4]


permu_cambio_2 =     [14, 17, 11, 24,  1,  5,
                       3, 28, 15,  6, 21, 10,
                      23, 19, 12,  4, 26,  8,
                      16,  7, 27, 20, 13,  2,
                      41, 52, 31, 37, 47, 55,
                      30, 40, 51, 45, 33, 48,
                      44, 49, 39, 56, 34, 53,
                      46, 42, 50, 36, 29, 32]

extension = [32,  1,  2,  3,  4,  5,
              4,  5,  6,  7,  8,  9,
              8,  9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32,  1]

P =[16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]


s_1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s_2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

s_3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

s_4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2 ,12 ,1 ,10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

s_5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

s_6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

s_7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s_8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]


corrimiento_izq = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

msn = "0123456789ABCDEF"
key = "133457799BBCDFF1"

letras_hex = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


def format(cadena,n):
    if n ==4:
        return ' '.join([cadena[i:i+4] for i in range(0, len(cadena), 4)])
    elif n ==6:
        return ' '.join([cadena[i:i+6] for i in range(0, len(cadena), 6)])
    elif n ==7:
        return ' '.join([cadena[i:i+7] for i in range(0, len(cadena), 7)])
    elif n ==8:
        return ' '.join([cadena[i:i+8] for i in range(0, len(cadena), 8)])
    

def encripta(texto):
    texto_bin = r = l = key_bin = c = d = c_cor = d_cor = total_cd = L_n = R_n = Expand_R = str_s1 = str_s2 = str_s3 = str_s4 = str_s5 = str_s6 = str_s7 = str_s8 = ""
    #Lee el mensaje
    for letra in texto:
        if letra in letras_hex:
            i = letras_hex[letra]
            bits_mod = bin(i)[2:].zfill(4)
            texto_bin += bits_mod
            if i >= 8:
                r += bits_mod
            else:
                l += bits_mod
    #print(f"\nL = {format(l,8)}" + "\n" f"R = {format(r,8)}")
    # Genera la llave
    for k in key:
        if k in letras_hex:
            key_bin += bin(letras_hex[k])[2:].zfill(4)

    #print(f"Key = {format(key_bin,8)}" + "\n")

    # Hace permutación a la llave
    new_key = ['0'] * len(permu_cambio_1)  
    for i, pc_1 in enumerate(permu_cambio_1):
        new_key[i] = key_bin[pc_1 - 1]
    new_key = ''.join(new_key)

    # Divide la llave en c,d
    for seg in range(len(new_key)):
        if seg >= 28:
            d += new_key[seg]
        else:
            c += new_key[seg]
    #print(f"New Key = {format(new_key,7)}")
    #print(f"C0 = {format(c,7)}" + "\n" f"D0 = {format(d,7)}")

    # Permuta IP con el mensaje 
    texto_per = ['0'] * len(init_permuta)
    for i, ip in enumerate(init_permuta):
        texto_per[i] = texto_bin[ip - 1]
    texto_per = ''.join(texto_per)

    #print(f"Msn_p = {format(texto_per,4)}" + "\n")

    # Divide el mensaje permutado en L,R
    for seg in range(len(texto_per)):
        if seg >= 32:
            R_n += texto_per[seg]
        else:
            L_n += texto_per[seg]

    #print(f"L0 = {format(L_n,4)}" + "\n" f"R0 = {format(R_n,4)}")

    # Guarda datos en una lista 
    L_cont = [L_n]  
    R_cont = [R_n]  
    C_cont = [c]    
    D_cont = [d]    
    Sk_cont = []   

    for ronda in range(1, 17):
        #print(f"\n------- Ronda {ronda} -------")
        # Hace el corrimiento a la izquierda
        shift = corrimiento_izq[ronda-1]
        
        c_next = C_cont[ronda-1][shift:] + C_cont[ronda-1][:shift]
        d_next = D_cont[ronda-1][shift:] + D_cont[ronda-1][:shift]
        
        C_cont.append(c_next)
        D_cont.append(d_next)
        
        #print(f"C{ronda} = {format(c_next,7)}" + "\n" + f"D{ronda} = {format(d_next,7)}")
        total_cd = c_next + d_next
        
        # Hace la PC-2 con el corrimiento y genera la llave permutada
        s_k = ['0'] * len(permu_cambio_2)
        for i, pc_2 in enumerate(permu_cambio_2):
            s_k[i] = total_cd[pc_2 - 1]
        s_k = ''.join(s_k)
        
        Sk_cont.append(s_k)
        #print(f"S_k{ronda} = {s_k}" + "\n")

        # Expande R
        Expand_R = ['0'] * len(extension)
        for i, ex in enumerate(extension):
            Expand_R[i] = R_cont[ronda-1][ex - 1]
        Expand_R = ''.join(Expand_R)
        
        # Sk XOR Rn
        sk_0b = int(s_k, 2)
        Rn_0b = int(Expand_R, 2)
        
        xor_r = sk_0b ^ Rn_0b
        xor_r_str = bin(xor_r)[2:].zfill(48)
        #print(f"\nSk{ronda}    {format(s_k,6)}")
        #print(f"ERn{ronda}   {format(Expand_R,6)}")
        #print(f"Res{ronda} = {format(xor_r_str,6)}")

        # Genera los bloques S
        for i in range(0, len(xor_r_str), 6):
            bloque_s = xor_r_str[i:i+6]
            
            ts1z = bloque_s[:1]
            ts4 = bloque_s[1:5]
            ts1d = bloque_s[-1:]
            
            es_t = ts1z + ts1d
            
            ts4_int = int(ts4, 2)
            es_t_int = int(es_t, 2)
            
            if i == 0:
                pos = s_1[es_t_int][ts4_int]
                str_s1 = bin(pos)[2:].zfill(4)
            elif i == 6:
                pos = s_2[es_t_int][ts4_int]
                str_s2 = bin(pos)[2:].zfill(4)
            elif i == 12:
                pos = s_3[es_t_int][ts4_int]
                str_s3 = bin(pos)[2:].zfill(4)
            elif i == 18:
                pos = s_4[es_t_int][ts4_int]
                str_s4 = bin(pos)[2:].zfill(4)
            elif i == 24:
                pos = s_5[es_t_int][ts4_int]
                str_s5 = bin(pos)[2:].zfill(4)
            elif i == 30:
                pos = s_6[es_t_int][ts4_int]
                str_s6 = bin(pos)[2:].zfill(4)
            elif i == 36:
                pos = s_7[es_t_int][ts4_int]
                str_s7 = bin(pos)[2:].zfill(4)
            else:
                pos = s_8[es_t_int][ts4_int]
                str_s8 = bin(pos)[2:].zfill(4)
        
        st = str_s1 + str_s2 + str_s3 + str_s4 + str_s5 + str_s6 + str_s7 + str_s8
        
        #print(f"Sf{ronda} = {format(st,4)}" + "\n")

        # Aplica la permutación P al bloque S
        st_per = ['0'] * len(P)
        for i, per in enumerate(P):
            st_per[i] = st[per - 1]
        st_per = ''.join(st_per)
    
        # Bloque S permutado XOR L_n
        st_0b = int(st_per, 2)
        Ln_0b = int(L_cont[ronda-1], 2)
        
        xor_l = st_0b ^ Ln_0b
        xor_l_str = bin(xor_l)[2:].zfill(32)
        
        #print("\n" f"Sfp{ronda}   {format(st_per,4)}")
        #print(f"L{ronda-1}     {format(L_cont[ronda-1],4)}")
        #print(f"Res{ronda} = {format(xor_l_str,4)}\n")

        L_next = R_cont[ronda-1]
        R_next = xor_l_str
        
        L_cont.append(L_next)
        R_cont.append(R_next)

    # Obtiene el resultado
    final_result = R_cont[16] + L_cont[16]  
    
    #print("\n----- RESULTADO FINAL ENCRIPTADO -----")
    #print(f"L16 = {format(L_cont[16],4)}")
    #print(f"R16 = {format(R_cont[16],4)}")
    #print(f"L16 (+) R16  = {format(final_result,4)}"+ "\n")

    final_res_per = ['0'] * len(init_per_inv)
    for i, per in enumerate(init_per_inv):
        final_res_per[i] = final_result[per - 1]
    final_res_per = ''.join(final_res_per)
    
    print(f"\nCifrado Bin: {format(final_res_per,4)}")
    final_dec = ""
    for y in range(0, len(final_res_per), 4):
        fin_0b4 = final_res_per[y:y+4]
        final_dec_4 = int(fin_0b4, 2)
        for item, val in letras_hex.items():
            if val == final_dec_4:
                final_dec += item
    print(f"Texto cifrado  {format(final_dec,4)}")
    print("___________"*9+"\n")
    return final_res_per, Sk_cont 
    
   
def desencripta(texto_cifrado, subkeys):

    L_n = R_n = Expand_R = str_s1 = str_s2 = str_s3 = str_s4 = str_s5 = str_s6 = str_s7 = str_s8 = ""

    # Aplica permutación IP a el texto cifrado
    texto_per = ['0'] * len(init_permuta)
    for i, ip in enumerate(init_permuta):
        texto_per[i] = texto_cifrado[ip - 1]
    texto_per = ''.join(texto_per)

    # Lo divide en L y R
    for seg in range(len(texto_per)):
        if seg >= 32:
            R_n += texto_per[seg]
        else:
            L_n += texto_per[seg]

    L_cont = [L_n]
    R_cont = [R_n]
    
    x = 15 # contador de ronda
    # HAce las 16 rondas
    for ronda in range(1, 17):
        #print(f"\n------- Ronda {ronda+x} -------")
        s_k = subkeys[16 - ronda]
        
        Expand_R = ['0'] * len(extension)
        for i, ex in enumerate(extension):
            Expand_R[i] = R_cont[ronda-1][ex - 1]
        Expand_R = ''.join(Expand_R)
        
        # Sk XOR Rn
        sk_0b = int(s_k, 2)
        Rn_0b = int(Expand_R, 2)
        
        xor_r = sk_0b ^ Rn_0b
        xor_r_str = bin(xor_r)[2:].zfill(48)
        #print(f"\nSk{ronda+x}    {format(s_k,6)}")
        #print(f"ERn{ronda+x}   {format(Expand_R,6)}")
        #print(f"Res{ronda+x} = {format(xor_r_str,6)}")

        # Obtiene los Bloques S
        for i in range(0, len(xor_r_str), 6):
            bloque_s = xor_r_str[i:i+6]
            
            ts1z = bloque_s[:1]
            ts4 = bloque_s[1:5]
            ts1d = bloque_s[-1:]
            
            es_t = ts1z + ts1d
            
            ts4_int = int(ts4, 2)
            es_t_int = int(es_t, 2)
            
            if i == 0:
                pos = s_1[es_t_int][ts4_int]
                str_s1 = bin(pos)[2:].zfill(4)
            elif i == 6:
                pos = s_2[es_t_int][ts4_int]
                str_s2 = bin(pos)[2:].zfill(4)
            elif i == 12:
                pos = s_3[es_t_int][ts4_int]
                str_s3 = bin(pos)[2:].zfill(4)
            elif i == 18:
                pos = s_4[es_t_int][ts4_int]
                str_s4 = bin(pos)[2:].zfill(4)
            elif i == 24:
                pos = s_5[es_t_int][ts4_int]
                str_s5 = bin(pos)[2:].zfill(4)
            elif i == 30:
                pos = s_6[es_t_int][ts4_int]
                str_s6 = bin(pos)[2:].zfill(4)
            elif i == 36:
                pos = s_7[es_t_int][ts4_int]
                str_s7 = bin(pos)[2:].zfill(4)
            else:
                pos = s_8[es_t_int][ts4_int]
                str_s8 = bin(pos)[2:].zfill(4)
        
        st = str_s1 + str_s2 + str_s3 + str_s4 + str_s5 + str_s6 + str_s7 + str_s8
        
        # Aplica la permutación P al bloque S
        st_per = ['0'] * len(P)
        for i, per in enumerate(P):
            st_per[i] = st[per - 1]
        st_per = ''.join(st_per)
    
        # Bloque S XOR  L_n
        st_0b = int(st_per, 2)
        Ln_0b = int(L_cont[ronda-1], 2)
        
        xor_l = st_0b ^ Ln_0b
        xor_l_str = bin(xor_l)[2:].zfill(32)
        
        #print("\n" f"Sfp{ronda+x}   {format(st_per,4)}")
        #print(f"L{ronda+x}     {format(L_cont[ronda-1],4)}")
        #print(f"Res{ronda+x} = {format(xor_l_str,4)}\n")

        L_next = R_cont[ronda-1]
        R_next = xor_l_str
        
        L_cont.append(L_next)
        R_cont.append(R_next)

        x -= 2 #variable para ronda


    final_result = R_cont[16] + L_cont[16]

    #print("\n----- RESULTADO FINAL -----")
    #print(f"L0 = {format(L_cont[16],4)}")
    #print(f"R0 = {format(R_cont[16],4)}"+ "\n")
    #print(f"L0 (+) R0  = {format(final_result,4)}"+ "\n")

    final_res_per = ['0'] * len(init_per_inv)
    for i, per in enumerate(init_per_inv):
        final_res_per[i] = final_result[per - 1]
    final_res_per = ''.join(final_res_per)

    print(f"\nDescifrado Bin: {format(final_res_per,4)}")

    final_dec = ""
    for y in range(0, len(final_res_per), 4):
        fin_0b4 = final_res_per[y:y+4]
        final_dec_4 = int(fin_0b4, 2)
        for item, val in letras_hex.items():
            if val == final_dec_4:
                final_dec += item
    print(f"Texto descifrado:  {format(final_dec,4)}")
    print("___________"*9+"\n")
    return final_res_per

print(f"\nMensaje: {msn}")
print(f"Key: {key}\n")
cifra, llaves = encripta(msn)
descifra = desencripta(cifra, llaves)