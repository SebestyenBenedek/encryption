def custom_decoder(obj):
    if '__bytearray__' in obj:
        return bytearray(obj['__bytearray__'])
    return obj