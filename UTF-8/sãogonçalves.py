def unicode_to_utf8(code_point):
    if code_point <= 0x7F:
        return bytes([code_point])
    elif code_point <= 0x7FF:
        return bytes([(0xC0 | (code_point >> 6)), (0x80 | (code_point & 0x3F))])
    elif code_point <= 0xFFFF:
        return bytes([(0xE0 | (code_point >> 12)), (0x80 | ((code_point >> 6) & 0x3F)), (0x80 | (code_point & 0x3F))])
    elif code_point <= 0x10FFFF:
        return bytes([(0xF0 | (code_point >> 18)), (0x80 | ((code_point >> 12) & 0x3F)), (0x80 | ((code_point >> 6) & 0x3F)), (0x80 | (code_point & 0x3F))])
    else:
        raise ValueError("Invalid Unicode code point")

def utf8_encode(string):
    utf8_bytes = b''
    for char in string:
        code_point = ord(char)
        utf8_bytes += unicode_to_utf8(code_point)
    return utf8_bytes

string = "São Gonçalves"

utf8_bytes = utf8_encode(string)
print(utf8_bytes)

'''
nesse codigo existe caracteres unicode como  ã  ç - eles precisam de duas sequencias de bytes para representar em utf-8.
a maioria são caracteres ASCII e portanto só precisam de um unico byte.

"ã" é um caractere Unicode que requer mais de um byte para ser representado em UTF-8. 
Ele é representado por duas sequências de bytes: 0xC3 0xA3.

"ç" é um caractere Unicode que requer mais de um byte para ser representado em UTF-8. 
Ele é representado por duas sequências de bytes: 0xC3 0xA7.

O restante é um caractere Unicode que necessita de apenas uma sequencia de bytes.
exemplo: "a" é um caractere ASCII e é representado por um único byte, que é 0x61 em hexadecimal ou 97 em decimal.

representação UTF-8 da string "São Gonçalves" é b'S\xc3\xa3o Gon\xc3\xa7alves'. Cada sequência de bytes representa um caractere individual na string original.

UTF-8 é uma codificação flexível e eficiente que permite representar uma ampla gama de caracteres Unicode usando sequências de bytes variáveis
'''