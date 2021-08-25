def _int32_to_bytes(i):
    return bytes((i & 0Xff,
    i >> 8 & 0xff ,
    i >> 16 & 0xff,
    i >> 24 & 0xff))