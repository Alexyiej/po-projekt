def convert(number):
    chars = "0123456789ABCDEF"
    hex_representation = ""
    while number > 0:
        rest = number % 16
        hex_representation = chars[rest] + hex_representation
        number //= 16
        
    return hex_representation