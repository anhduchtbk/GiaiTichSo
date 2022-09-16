"""
 C = (F - 32) / 1.8
"""    

def convert(F):
    return int((F - 32.0) / 1.8)

print(convert(69.8))