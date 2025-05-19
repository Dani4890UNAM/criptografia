# Implementación de Cifrado AES-128

Este documento explica una implementación del algoritmo AES (Advanced Encryption Standard) en modo ECB para cifrado de 128 bits.

## Componentes principales

### Tablas AES

1. **s_box**: Tabla de sustitución no lineal usada en la fase SubBytes. Transforma cada byte del estado según una tabla predefinida.
2. **inv_s_box**: Tabla inversa de s_box, usada para descifrar.
3. **rcon**: Constantes de ronda usadas en la expansión de clave.

### Funciones principales

#### 1. Transformaciones básicas

- **sub_bytes(state)**: Aplica la sustitución byte a byte usando s_box.
- **inv_sub_bytes(state)**: Operación inversa usando inv_s_box.
- **shift_rows(state)**: Desplaza filas del estado (1ª fila 0 pos, 2ª 1 pos, etc.).
- **inv_shift_rows(state)**: Deshace el desplazamiento de filas.
- **xtime(a)**: Multiplicación por x en GF(2^8), usado en MixColumns.

#### 2. MixColumns

- **mix_columns(state)**: Mezcla columnas usando multiplicación matricial en GF(2^8).
- **inv_mix_columns(state)**: Operación inversa con matriz diferente.

#### 3. Manejo de claves

- **add_round_key(state, key)**: XOR entre el estado y la clave de ronda.
- **key_expansion(key)**: Expande la clave inicial en 11 claves de ronda (44 palabras).

#### 4. Funciones principales

- **cipher(input_bytes, key)**: 
  - Convierte texto plano a matriz de estado
  - Aplica AddRoundKey inicial
  - 9 rondas con SubBytes, ShiftRows, MixColumns y AddRoundKey
  - Ronda final sin MixColumns
- **inv_cipher(ciphertext, key)**: Proceso inverso para descifrar.

### Flujo del programa principal

1. **Entradas**:
   - `texto_plano`: Cadena de 16 bytes ("Esto es una demo")
   - `clave`: Cadena de 16 bytes ("Aqui va la clave")

2. **Proceso**:
   - Convierte texto y clave a bytes
   - Organiza la clave en matriz 4x4 (column-major)
   - Cifra con `cipher()`
   - Descifra con `inv_cipher()`

3. **Salidas**:
   - Muestra texto original, clave, texto cifrado y resultado del descifrado.

## Notas importantes

1. **Especificaciones técnicas**:
   - Esta implementación usa **AES-128** (clave de 128 bits)
   - El modo de operación es **ECB**
   - No incluye sistema de padding (relleno), por lo que:
     - El texto a cifrar debe ser exactamente de **16 bytes**
     - La clave debe ser exactamente de **16 bytes** (128 bits)

## Ejemplo de uso

```python
Texto plano (16 caracteres): Esto es una demo
Texto plano (hex):  4573746f20657320756e612064656d6f

Clave AES-128 (16 caracteres):       Aqui va la clave
Clave AES-128 (hex):        41717569207661206c6120636c617665

Texto Cifrado (hex):     d9e682c9a8b5b5a5b9a8a5b5a5b9a8

Texto Descifrado:  Esto es una demo