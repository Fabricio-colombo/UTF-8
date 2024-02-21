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

string = "ç - ã - õ - á - ó - ú >>"

utf8_bytes = utf8_encode(string)
print(utf8_bytes)


# b'\xc3\xa7 - \xc3\xa3 - \xc3\xb5 - \xc3\xa1 - \xc3\xb3 - \xc3\xba >>'
#utf-8 para caracteres é usado uma sequencia de 2 bytes ou 16 bits

#para ASCII é usado uma sequencia de 1 byte ou 8 bits.